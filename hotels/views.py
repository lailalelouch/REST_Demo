from datetime import datetime

from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView

from .models import Hotel, Booking
from .serializers import HotelsListSerializer, BookingDetailsSerializer, HotelDetailsSerializer, BookHotelSerializer, UserCreateSerializer


class HotelsList(ListAPIView):
	queryset = Hotel.objects.all()
	serializer_class = HotelsListSerializer


class BookingsList(ListAPIView):
	serializer_class = BookingDetailsSerializer

	def get_queryset(self):
		today = datetime.today()
		return Booking.objects.filter(user=self.request.user, check_in__gte=today)


class HotelDetails(RetrieveAPIView):
	queryset = Hotel.objects.all()
	serializer_class = HotelDetailsSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'hotel_id'


class ModifyBooking(RetrieveUpdateAPIView):
	queryset = Booking.objects.all()
	serializer_class = BookHotelSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'booking_id'	


class CancelBooking(DestroyAPIView):
	queryset = Booking.objects.all()
	lookup_field = 'id'
	lookup_url_kwarg = 'booking_id'


class BookHotel(CreateAPIView):
	serializer_class = BookHotelSerializer

	def perform_create(self, serializer):
		serializer.save(user=self.request.user, hotel_id=self.kwargs['hotel_id'])


class Register(CreateAPIView):
    serializer_class = UserCreateSerializer