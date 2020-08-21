# CARS/views.py

from django.shortcuts import render, get_object_or_404
from cars.models import Car 
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator 

# Create your views here.
# def cars(request):
# 	cars = Car.objects.order_by('-created_date')
# 	data = {
# 		'cars':cars
# 	}
# 	return render(request, 'cars/cars.html', data)

# STEPS creating paginator for dedicated cars page with paginator
def cars(request):
	#1. Get all page order by created date and store them in cars variable
	cars = Car.objects.order_by('-created_date')
	#2. Get 3 from all cars
	paginator = Paginator(cars, 4)
	#3. Get the page and store it in page variable
	page = request.GET.get('page') 
	#4. Store the page in paged_cars 
	paged_cars = paginator.get_page(page)
	#5. Store now the page in data
	data = {
		'cars':paged_cars,
	}
	return render(request, 'cars/cars.html', data)

def car_detail(request, id):
	single_car = get_object_or_404(Car, pk=id)
	data = {
		'single_car':single_car
	}
	return render(request, 'cars/car_detail.html', data)

