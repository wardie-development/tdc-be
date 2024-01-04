from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from apps.orderlist.models import CellphoneModel
from apps.orderlist.serializers import CellphoneModelSerializer, CreateOrderSerializer


class CellphoneModelViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    GenericViewSet
):
    queryset = CellphoneModel.objects.all()
    serializer_class = CellphoneModelSerializer

    def get_serializer_class(self):
        if self.action == "create":
            return CreateOrderSerializer
        return super().get_serializer_class()
