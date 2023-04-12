from django.urls import include, path
from .views import RestaurantDetail, RestaurantList
from .views import MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('restaurants/', RestaurantList.as_view()),
    path('restaurants/<int:pk>/', RestaurantDetail.as_view()),]

urlpatterns += [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]