from rest_framework import serializers
from .models import Menu


class MenuSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.user')

    class Meta:
        model = Menu
        fields = '__all__'
    


