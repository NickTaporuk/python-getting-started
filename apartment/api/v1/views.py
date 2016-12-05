from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
)

from apartment.models import Apartment

from .serializers import (
    ApartmentListSerializer,
    ApartmentDetailSerializer,
)
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,

)


class ApartmentListAPIView(ListAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentListSerializer
    permission_classes = [IsAuthenticated]

class ApartmentDetailAPIView(RetrieveAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentDetailSerializer
