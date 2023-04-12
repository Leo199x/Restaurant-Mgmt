from rest_framework import serializers
from .models import Restaurant

class RestaurantSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True, allow_blank=False, max_length=100)
    address = serializers.CharField(required=True, allow_blank=False, max_length=100)
    description = serializers.CharField(required=False, allow_blank=True, max_length=100)

    #owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Restaurant
        fields = '__all__'
    

