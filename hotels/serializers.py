from rest_framework import serializers

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