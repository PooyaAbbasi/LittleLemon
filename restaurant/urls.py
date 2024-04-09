from django.urls import path
from .views import *

app_name = 'restaurant'

urlpatterns = [
    path('home/', home_page, name='home-page'),
    path('menu/', MenuList.as_view(), name='menu-list'),
    path('menu/<int:pk>/', MenuDetail.as_view(), name='menu-detail'),

]
