# CARS/views.py

from django.shortcuts import render
from cars import views

# Create your views here.
def cars(request):
	return render(request, 'cars/cars.html')