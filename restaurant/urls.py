from django.urls import path
from .views import *

app_name = 'restaurant'

urlpatterns = [
    path('home/', home_page, name='home-page')
]
