from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import bookingform
from .models import booking
# Create your views here.

def about(request):
	return render(request, 'main/about.html')




def all_bookings(request):
	booking_list = booking.objects.all()
	return render(request, 'main/bookinglist.html', {'booking_list': booking_list})


def booking_form(request):
	submitted = False
	if request.method == "POST":
		form = bookingform(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/booking_form?submitted=True')

	else:
		form = bookingform
		if 'submitted' in request.GET:
			submitted = True

	return render(request, 'main/bookingform.html', {'form':form, 'submitted':submitted})

def home(request):
	return render(request, 'main/home.html')


def login_user(request):
	return render(request, 'app_user/login.html')

def reset_password(request):
	return render(request, 'app_user/password_reset_form.html')
