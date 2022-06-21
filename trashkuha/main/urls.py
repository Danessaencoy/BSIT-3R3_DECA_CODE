from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('booking_form', views.booking_form, name="booking-form"),
    path('booking_list', views.all_bookings, name="booking-list"),
    path('about', views.about, name="about"),

   
    
]
