from rest_framework.generics import (
    ListAPIView,
)

from apartment.models import Apartment

from .serializers import (
    ApartmentListSerializer
)


class PostListAPIView(ListAPIView):
    serializer_class = ApartmentListSerializer