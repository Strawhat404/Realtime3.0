from rest_framework import serializers
from .models import Area, Promotion

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ['id', 'name', 'major']

class PromotionSerializer(serializers.ModelSerializer):
    area = AreaSerializer(read_only=True)
    area_id = serializers.PrimaryKeyRelatedField(queryset=Area.objects.all(), source='area', write_only=True)

    class Meta:
        model = Promotion
        fields = ['id', 'area', 'area_id', 'content', 'active']