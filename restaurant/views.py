from django.shortcuts import render
from restaurant.permissions import IsOwnerOrReadOnly, IsAdmin
from .models import Restaurant
from rest_framework import generics, permissions
from .serializers import RestaurantSerializer

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
# Create your views here.

class RestaurantList(generics.ListCreateAPIView):
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsAdmin]


    #def perform_create(self, serializer):
        #serializer.save(owner=self.request.user)

class RestaurantDetail(generics.RetrieveAPIView):
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()




class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['email'] = user.email
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

