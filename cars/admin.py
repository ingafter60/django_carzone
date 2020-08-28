# cars/admin.py
from django.contrib import admin
from cars.models import Car 
from django.utils.html import format_html

# Register your models here.

class CarAdmin(admin.ModelAdmin):
	def thumbnail(self, object):
		return format_html('<img src="{}" width="40" style="border-radius:50px;" />', format(object.car_photo.url))

	thumbnail.short_description = 'Car Image'
	list_display = ('id', 'thumbnail', 'car_title', 'price', 'city', 'color', 'model', 'year', 'body_style', 'fuel_type', 'is_featured')
	list_display_links = ('id', 'thumbnail', 'car_title')
	list_editable = ('is_featured',)
	search_field = ('id', 'car_title', 'city', 'model', 'body_style', 'fuel_type')
	list_filter = ('city', 'model', 'body_style', 'fuel_type')

	
	# Display year in sequance (2016, 2017, 20..)
	def get_queryset(self, request):
		queryset = super(CarAdmin, self).get_queryset(request)
		queryset = queryset.order_by('year')
		return queryset

admin.site.register(Car, CarAdmin)