from django.urls import include, path
from rest_framework import routers
from .views import MenuViewSet

router = routers.DefaultRouter()
router.register('menus', MenuViewSet)

urlpatterns = [
    path('', include((router.urls, 'menus'), namespace='menu')),


]
