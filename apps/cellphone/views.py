from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.cellphone.models import Brand
from apps.cellphone.permissions import IsAuthenticated
from apps.cellphone.serializers import BrandSerializer, \
    CellphoneAuthenticationSerializer


class BrandViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=["post"])
    def authenticate(self, request):
        serializer = CellphoneAuthenticationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.save()

        return Response({"token": token.token})

    @action(detail=False, methods=["get"], url_path="name")
    def list_name(self, request):
        names = Brand.objects.values("name")

        return Response(names)
