# ACCOUNTS/views.py
from django.shortcuts import render, redirect
from django.contrib import messages

def login(request):

	data = {
		'login_page':'active'
	}

	return render(request, 'accounts/login.html')

# STATIC template
# def register(request):

# 	data = {
# 		'register_page':'active'
# 	}
		
# 	return render(request, 'accounts/register.html')


# CHECKING if POST request is working or not
# def register(request):

# 	if request.method == 'POST':
# 		print('this is POST request')
# 		return redirect('register')

# 	else: 
		
# 		return render(request, 'accounts/register.html')


# CHECKING if alert message is working or not
def register(request):

	if request.method == 'POST':
		messages.error(request, 'this is error message you know!')
		return redirect('register')

	else: 
		
		return render(request, 'accounts/register.html')








def dashboard(request):
	return render(request, 'accounts/dashboard.html')


def logout(request):
	return redirect('home')	
