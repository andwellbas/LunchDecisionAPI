from django.urls import path
from . import views

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path("restaurants/", views.RestaurantListCreateView.as_view(), name="restaurant"),
    path("menus/", views.MenuListCreateView.as_view(), name="menu"),
    path("votes/", views.VoteCreateView.as_view(), name="vote"),
    path("employees/", views.EmployeeListCreateView.as_view(), name="employee-list"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
