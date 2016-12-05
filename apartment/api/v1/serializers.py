from rest_framework.serializers import (
    ModelSerializer
)
from apartment.models import Apartment


class ApartmentListSerializer(ModelSerializer):
    class Meta:
        model = Apartment
        fields = [
            'detailsInfoJson',
        ]


class ApartmentDetailSerializer(ModelSerializer):
    class Meta:
        model = Apartment
        fields = [
            'detailsInfoJson',
        ]