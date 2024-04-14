from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView, CreateView
from .forms import BookingForm
from django.urls import reverse_lazy

# Create your views here.


def home_page(request):
    context = {}
    return render(request, 'restaurant/home-page.html', context)


class MenuList(ListView):
    model = Menu
    template_name = 'restaurant/menu.html'
    template_name_suffix = ''
    ListView.context_object_name = 'menu_items'


class MenuDetail(DetailView):
    model = Menu
    template_name = 'restaurant/menu-item-detail.html'
    context_object_name = 'menu'


class BookingCreateView(CreateView):
    model = Booking
    template_name = 'restaurant/booking.html'
    form_class = BookingForm
    context_object_name = 'booking_form'
    success_url = reverse_lazy('restaurant:successful-booking')


def successful_booking(request):

    return render(request, 'restaurant/successful-booking.html')


class BookingDetail(DetailView):
    model = Booking
    template_name = 'restaurant/booking-detail.html'
    context_object_name = 'booking'


class BookingList(ListView):
    model = Booking
    context_object_name = 'booking_list'


