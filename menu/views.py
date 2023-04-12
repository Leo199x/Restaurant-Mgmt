from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MenuSerializer
from .models import Menu


# Create your views here.
class MenuViewSet(viewsets.ModelViewSet):
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()
    
    
