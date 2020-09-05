# ACCOUNTS/views.py
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

"""
=================USER LOGIN START=============
"""

# 1. Static
# def login(request):

# 	data = {
# 		'login_page':'active'
# 	}

# 	return render(request, 'accounts/login.html')

# # 2. Dynamic
def login(request):

	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = auth.authenticate(username=username, password=password)

		# If usename and password exists
		if user is not None:
			auth.login(request, user)
			messages.success(request, 'You are now logged in!')
			return redirect('dashboard')

		# If usename and password exists/invalid
		else:
			messages.error(request, 'Invalid login credentials')
			return redirect('login')

	data = {
		'login_page':'active'
	}			

	return render(request, 'accounts/login.html', data)

"""
=================USER LOGIN END=============
"""

"""
=================USER REGISTRATION START=============
"""

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


# # CHECKING if alert message is working or not
# def register(request):

# 	if request.method == 'POST':
# 		messages.error(request, 'this is error message you know!')
# 		return redirect('register')

# 	else: 
		
# 		return render(request, 'accounts/register.html')


# 48/56. User Registration
def register(request):

	data = {
		'register_page':'active',
	}

	if request.method == 'POST':
		firstname			= request.POST['firstname']
		lastname				= request.POST['lastname']
		username				= request.POST['username']
		email					= request.POST['email']
		password				= request.POST['password']
		confirm_password	= request.POST['confirm_password']

		# CHECKING
		#1 If  password and confirm password is the same
		if password == confirm_password:
			#2 If the user name is already exists
			if User.objects.filter(username=username).exists():
				messages.error(request, 'That username already exists! Use other name.')
				return redirect('register')
			
			#3 If the email is already exist
			else:
				if User.objects.filter(email=email).exists():
					messages.error(request, 'That email already exists! Use other email.')
					return redirect('register')
				#4 If usename and email do not exist, create user
				else:
					user = User.objects.create_user(
									first_name=firstname,
									last_name=lastname,
									username=username,
									email=email,
									password=password)
					#5 Login directly after successfully register
					auth.login(request, user)
					messages.success(request, 'You are logged in!')
					return redirect('dashboard')

					user.save()
					messages.success(request, 'You are registered successfully!')
					return redirect('login')					

		else:
			messages.error(request, 'Password do not match!')
			return redirect('register')

	else: 

		return render(request, 'accounts/register.html', data)

"""
=================USER REGISTRATION END=============
"""

"""
=================USER DASHBOARD START=============
"""
def dashboard(request):

	data = {
		'dashboard_page':'active'
	}	

	return render(request, 'accounts/dashboard.html', data)

"""
=================USER DASHBOARD END=============
"""


"""
=================USER LOGOUT START=============
"""
def logout(request):

	if request.method == 'POST':
		auth.logout(request)
		# messages.success(request, 'You are successfully logged out!')
		return redirect('home')	
	return redirect('home')	

"""
=================USER LOGOUT END=============
"""