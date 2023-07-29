from rest_framework import serializers
from .models import Restaurant, Menu, Employee


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = "__all__"


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = "__all__"


class VoteSerializer(serializers.Serializer):
    menu_id = serializers.IntegerField()


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"
