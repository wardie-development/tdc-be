from rest_framework import viewsets

from apps.cellphone.models import Cellphone
from apps.cellphone.serializers import CellphoneSerializer


class CellphoneViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Cellphone.objects.all()
    serializer_class = CellphoneSerializer
