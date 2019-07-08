from datetime import datetime

from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Hotel, Booking
from .serializers import HotelsListSerializer, BookingDetailsSerializer, HotelDetailsSerializer, BookHotelSerializer, UserCreateSerializer
from .permissions import IsBookedByUser, IsNotInPast


class HotelsList(ListAPIView):
	queryset = Hotel.objects.all()
	serializer_class = HotelsListSerializer
	filter_backends = [SearchFilter, OrderingFilter]
	search_fields = ['name', 'location']


class BookingsList(ListAPIView):
	serializer_class = BookingDetailsSerializer
	permission_classes = [IsAuthenticated]

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
	permission_classes = [IsAuthenticated, IsBookedByUser, IsNotInPast]


class CancelBooking(DestroyAPIView):
	queryset = Booking.objects.all()
	lookup_field = 'id'
	lookup_url_kwarg = 'booking_id'
	permission_classes = [IsAuthenticated, IsBookedByUser, IsNotInPast]


class BookHotel(CreateAPIView):
	serializer_class = BookHotelSerializer
	permission_classes = [IsAuthenticated]

	def perform_create(self, serializer):
		serializer.save(user=self.request.user, hotel_id=self.kwargs['hotel_id'])


class Register(CreateAPIView):
    serializer_class = UserCreateSerializer