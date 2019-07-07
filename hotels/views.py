from datetime import datetime

from rest_framework.generics import ListAPIView

from .models import Hotel, Booking
from .serializers import HotelsListSerializer, BookingDetailsSerializer


class HotelsList(ListAPIView):
	queryset = Hotel.objects.all()
	serializer_class = HotelsListSerializer


class BookingsList(ListAPIView):
	queryset = Booking.objects.filter(check_in__gte=datetime.today())
	serializer_class = BookingDetailsSerializer
