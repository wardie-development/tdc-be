from rest_framework import serializers
from rest_framework.generics import get_object_or_404

from apps.orderlist.models import CellphoneModel, Order


class CellphoneModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CellphoneModel
        fields = ('name',)


class CreateOrderSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    whatsapp = serializers.CharField(max_length=255)
    message = serializers.CharField(max_length=255)
    cellphone_models = serializers.ListField(
        child=serializers.DictField()
    )

    def create(self, validated_data):
        cellphone_models = validated_data.pop('cellphone_models')
        order = Order.objects.create(
            **validated_data
        )
        for cellphone_model in cellphone_models:
            cellphone_model_name = cellphone_model.pop('cellphone_model')
            cellphone_model_instance = get_object_or_404(
                CellphoneModel,
                name=cellphone_model_name
            )
            order.cellphone_models.create(
                cellphone_model=cellphone_model_instance,
                **cellphone_model
            )
        return order

    def to_representation(self, instance):
        return {
            "pdf_link": instance.pdf_link
        }
