# ACCOUNTS/views.py
from django.shortcuts import render, redirect


def login(request):

	data = {
		'login_page':'active'
	}

	return render(request, 'accounts/login.html')


def register(request):

	data = {
		'register_page':'active'
	}

	return render(request, 'accounts/register.html')


def dashboard(request):
	return render(request, 'accounts/dashboard.html')


def logout(request):
	return redirect('home')	
