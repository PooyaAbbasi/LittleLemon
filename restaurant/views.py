from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView


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
