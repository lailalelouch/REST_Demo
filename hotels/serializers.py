from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Hotel, Booking


class HotelsListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Hotel
		fields = ['name']


class BookingDetailsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = ["id" ,"hotel", "check_in", 'number_of_nights']


class HotelDetailsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Hotel
		fields = ["id", "name", "location", "price_per_night"]


class BookHotelSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = ['check_in', 'number_of_nights']


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        email = validated_data['email']
        new_user = User(username=username, email=email)
        new_user.set_password(password)
        new_user.save()
        return validated_data