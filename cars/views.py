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

	# Car search
	model_search = Car.objects.values_list('model', flat=True).distinct()
	city_search = Car.objects.values_list('city', flat=True).distinct()
	year_search = Car.objects.values_list('year', flat=True).distinct().order_by('year')
	body_style_search = Car.objects.values_list('body_style', flat=True).distinct()

	data = {
		'cars':paged_cars,
		# Car search
		'model_search': model_search,
		'city_search': city_search,
		'year_search': year_search,
		'body_style_search': body_style_search,		
	}
	return render(request, 'cars/cars.html', data)


def car_detail(request, id):
	single_car = get_object_or_404(Car, pk=id)
	data = {
		'single_car':single_car
	}
	return render(request, 'cars/car_detail.html', data)


# def search(request):
# 	cars = Car.objects.order_by('-created_date')

# 	data = {
# 		'cars':cars
# 	}
# 	return render(request, 'cars/search.html', data)

# SEARCH BASED-KEYWORD
def search(request):
	cars = Car.objects.order_by('-created_date')
	# Car search
	model_search = Car.objects.values_list('model', flat=True).distinct()
	city_search = Car.objects.values_list('city', flat=True).distinct()
	year_search = Car.objects.values_list('year', flat=True).distinct().order_by('year')
	body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
	transmission_search = Car.objects.values_list('transmission', flat=True).distinct()

	# if has keyword request from the url
	if 'keyword' in request.GET:
		keyword = request.GET['keyword']
		# check if keyword is not blank, find the keyword in the hole of the description
		if keyword:
			cars = cars.filter(description__icontains=keyword)

	# if has keyword request from the url
	if 'model' in request.GET:
		model = request.GET['model']
		# check if keyword is not blank, find the keyword in the hole of the description
		if model:
			cars = cars.filter(model__iexact=model)

	# if has keyword request from the url
	if 'city' in request.GET:
		city = request.GET['city']
		# check if keyword is not blank, find the keyword in the hole of the description
		if city:
			cars = cars.filter(city__iexact=city)

	# if has keyword request from the url
	if 'year' in request.GET:
		year = request.GET['year']
		# check if keyword is not blank, find the keyword in the hole of the description
		if year:
			cars = cars.filter(year__iexact=year)

	# if has keyword request from the url
	if 'body_style' in request.GET:
		body_style = request.GET['body_style']
		# check if keyword is not blank, find the keyword in the hole of the description
		if body_style:
			cars = cars.filter(body_style__iexact=body_style)

	# price range 
	if 'min_price' in request.GET:
		min_price = request.GET['min_price']
		max_price = request.GET['max_price']
		if max_price:
			cars = cars.filter(price__gte=min_price, price__lte=max_price)

	data = {
		'cars':cars,
		# Car search
		'model_search': model_search,
		'city_search': city_search,
		'year_search': year_search,
		'body_style_search': body_style_search,
		'transmission_search': transmission_search,		
	}
	return render(request, 'cars/search.html', data)

