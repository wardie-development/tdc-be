from django.db.models import OuterRef, F, Value, CharField
from django.db.models.functions import Concat
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import serializers

from apps.cellphone.models import (
    CellphoneAccess,
    CellphoneAccessToken,
    CellphoneSuggestion,
    Cellphone, Brand,
)


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ["name"]

    def to_representation(self, instance):
        request = self.context["request"]
        access = CellphoneAccessToken.objects.get(
            token=request.headers.get("Authorization")
        ).access

        queryset = (
            Cellphone.objects.filter(brand=instance).only("model", "compatibility_line")
        )

        if access.is_test_access:
            queryset = queryset.filter(is_visible_for_test=True)

        cellphones = [
            {
                "brand": instance.name,
                "model": item.model,
                "compatibilities": item.compatibility_line,
            }
            for item in queryset
        ]

        return {
            'title': f'Películas para {instance.name}',
            'color': instance.mapped_colors.get(instance.name, instance.mapped_colors["Samsung"]),
            'cellphones': cellphones,
        }


class CellphoneAuthenticationSerializer(serializers.Serializer):
    password = serializers.CharField()

    def validate(self, attrs):
        password = attrs.get("password")

        access = get_object_or_404(CellphoneAccess, password=password)

        if not access:
            raise serializers.ValidationError("Senha incorreta")

        if access.is_access_expired():
            raise serializers.ValidationError("Acesso expirado")

        return attrs

    def save(self, **kwargs):
        password = self.validated_data.get("password")
        access = get_object_or_404(CellphoneAccess, password=password)
        token = CellphoneAccessToken.objects.get_or_create(access=access)[0]
        token.renew_token_if_expired()
        return token


class CellphoneSuggestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CellphoneSuggestion
        fields = "__all__"


class CellphoneSerializer(serializers.Serializer):
    def to_representation(self, instance):
        access = self.context["access"]
        instance.news_views.add(access)
        instance.save()
        return instance.to_representation()
