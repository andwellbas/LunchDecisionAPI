from rest_framework import generics
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes

from .models import Restaurant, Menu, Employee
from .serializers import RestaurantSerializer, MenuSerializer, EmployeeSerializer, VoteSerializer


@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class RestaurantListCreateView(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    def perform_create(self, serializer):
        serializer.save()

    def get(self, request, *args, **kwargs):
        # get a list of all restaurants
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class MenuListCreateView(generics.ListCreateAPIView):
    serializer_class = MenuSerializer

    def get_queryset(self):
        requested_date = self.request.GET.get("date")
        restaurant_id = self.request.GET.get("restaurant")

        if requested_date and restaurant_id:
            # filtering by date and restaurant ID
            return Menu.objects.filter(date=requested_date, restaurant_id=restaurant_id)
        elif requested_date:
            # if the "date" parameter is passed, we filter the menu by this date
            return Menu.objects.filter(date=requested_date)
        else:
            # if no date parameter is passed, we return all menus
            return Menu.objects.all()

    def perform_create(self, serializer):
        restaurant_id = self.request.data.get("restaurant")
        restaurant = Restaurant.objects.get(id=restaurant_id)
        serializer.save(restaurant=restaurant)


@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class VoteCreateView(generics.CreateAPIView):
    serializer_class = VoteSerializer

    def create(self, request, *args, **kwargs):
        menu_id = request.data.get("menu_id")
        menu = Menu.objects.get(id=menu_id)
        # add vote to the menu
        menu.votes_count += 1
        menu.save()
        return Response({"'message': 'Vote has been counted successfully.'"})


@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def perform_create(self, serializer):
        serializer.save()

    def get(self, request, *args, **kwargs):
        # get a list of all employees
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
