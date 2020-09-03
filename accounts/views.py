# ACCOUNTS/views.py
from django.shortcuts import render, redirect


def login(request):

	data = {
		'login_page':'active'
	}

	return render(request, 'accounts/login.html')


def register(request):

	if request.method == 'POST':
		print('this is POST request')
		return redirect('register')

	else: 
		
		return render(request, 'accounts/register.html')

	# data = {
	# 	'register_page':'active'
	# }



def dashboard(request):
	return render(request, 'accounts/dashboard.html')


def logout(request):
	return redirect('home')	
