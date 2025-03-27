from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import Area, Promotion
from .serializers import AreaSerializer, PromotionSerializer

class AreaListCreate(generics.ListCreateAPIView):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer
    permission_classes = [AllowAny]  # Adjust for prod

class PromotionListCreate(generics.ListCreateAPIView):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer
    permission_classes = [AllowAny]  # Adjust for prod