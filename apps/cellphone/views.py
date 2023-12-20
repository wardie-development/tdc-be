from datetime import timedelta

from django.utils import timezone
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.cellphone.models import Brand, Cellphone, CellphoneAccessToken, \
    CellphoneAccessLog, CellphoneAccessTry
from apps.cellphone.permissions import IsAuthenticated
from apps.cellphone.serializers import (
    BrandSerializer,
    CellphoneAuthenticationSerializer,
    CellphoneSuggestionsSerializer,
    CellphoneSerializer,
)


class BrandViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Brand.objects.filter(is_active=True).order_by("order")
    serializer_class = BrandSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        access = CellphoneAccessToken.objects.get(
            token=self.request.headers.get("Authorization")
        ).access

        if access.is_test_access:
            queryset = queryset.filter(cellphones__is_visible_for_test=True).distinct()

        return queryset

    @action(detail=False, methods=["post"])
    def authenticate(self, request):
        serializer = CellphoneAuthenticationSerializer(data=request.data)
        if serializer.is_valid():
            token = serializer.save()

            ip = request.META.get("REMOTE_ADDR")
            user_agent = request.META.get("HTTP_USER_AGENT")
            access = token.access

            if access.logs.count() >= access.access_limit:
                return Response(
                    {"message": "Limite de acessos atingido"},
                    status=403
                )

            access_log = CellphoneAccessLog.objects.get_or_create(
                access=access,
                ip=ip,
                user_agent=user_agent,
            )[0]
            access_log.token = token.token
            access_log.save()

            return Response({"token": token.token, "is_test_access": access.is_test_access})
        else:
            CellphoneAccessTry.objects.create(
                ip=request.META.get("REMOTE_ADDR"),
                user_agent=request.META.get("HTTP_USER_AGENT"),
                password_tryed=request.data.get("password"),
            )
            return Response(serializer.errors, status=400)

    @action(detail=False, methods=["get"], url_path="name")
    def list_name(self, request):
        access = CellphoneAccessToken.objects.get(
            token=request.headers.get("Authorization")
        ).access
        names = Brand.objects.only("name", "is_active", "order").filter(is_active=True).order_by("order").values("name")

        if access.is_test_access:
            names = names.filter(cellphones__is_visible_for_test=True).distinct()

        return Response(names)

    @action(detail=False, methods=["post"])
    def suggestion(self, request):
        serializer = CellphoneSuggestionsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"message": "Sugestão enviada com sucesso"})

    @action(detail=False, methods=["get"])
    def news(self, request):
        three_days_ago = timezone.now() - timedelta(days=3)
        access = CellphoneAccessToken.objects.get(
            token=request.headers.get("Authorization")
        ).access

        news = Cellphone.objects.filter(
            created_at__gte=three_days_ago
        ).exclude(
            news_views__whatsapp=access
        )

        if access.is_test_access:
            news = news.filter(is_visible_for_test=True)

        data = CellphoneSerializer(news, many=True, context={"access": access}).data

        return Response(data)
