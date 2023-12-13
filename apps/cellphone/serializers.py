from django.shortcuts import get_object_or_404
from rest_framework import serializers

from apps.cellphone.models import (
    CellphoneAccess,
    CellphoneAccessToken,
    CellphoneSuggestion,
    Cellphone,
)


class BrandSerializer(serializers.Serializer):
    def to_representation(self, instance):
        return instance.to_representation()


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
