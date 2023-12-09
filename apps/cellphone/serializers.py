from rest_framework import serializers

from apps.cellphone.models import Cellphone


class CellphoneSerializer(serializers.ModelSerializer):
    to_display = serializers.SerializerMethodField()

    class Meta:
        model = Cellphone
        fields = (
            "id",
            "to_display",
        )

    def get_to_display(self, obj):
        compatibilities = obj.cellphone_screen_protector_compatibilities.all()

        return {
            "brand": obj.brand.name,
            "model": obj.model,
            "compatibilities": [
                compatibility.name
                for compatibility in compatibilities
            ],
        }
