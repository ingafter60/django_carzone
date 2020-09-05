# CONTACTS/urls.py

from django.urls import path

from accounts import views

urlpatterns = [
	path('inquiry', views.inquiry, name="inquiry"),
]
