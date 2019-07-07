from rest_framework import serializers

from .models import Hotel, Booking


class HotelsListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Hotel
		fields = ['name']


class BookingDetailsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = ["hotel", "check_in", 'number_of_nights']