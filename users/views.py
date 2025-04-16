# Import necessary modules for user authentication and views
# Import Django shortcuts for rendering and redirecting
from django.shortcuts import render, redirect

# Import User model from users app

from .models import *

# Import Post model from posts app
from posts.models import *

# Import Django authentication system
# Import authenticate function to check user credentials
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

# Import Django messages system
# Use to display messages to users
from django.contrib import messages


# User registration view
def register(request):
    # Check if request method is POST
    if request.method == 'POST':
        # Get user input from form
        # why we use post.get()?
        # because we want to get the value of the input field with the name attribute
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')

        # Check if user already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered')
            return redirect('register')

        # Create new user
        # why we use create_user()?
        # because we want to create a new user with the given email, name, password, and phone
        user = User.objects.create_user(
            email=email, name=name, password=password, phone=phone)
        user.save()
        # why we use messages.success()?
        # because we want to display a success message to the user
        messages.success(request, 'Registration successful. Please login.')
        return redirect('login')

    return render(request, 'users/register.html')


# User login view
def login(request):
    # Check if request method is POST
    if request.method == 'POST':
        # Get user input from form
        email = request.POST.get('email')
        password = request.POST.get('password')
        # why we use authenticate()?
        # because we want to check if the user exists and the password is correct
        user = authenticate(request, email=email, password=password)
        if user is not None:
            # why we use auth_login()?
            # because we want to log the user in
            auth_login(request, user)
            return redirect('list_posts')  # redirect to a view or URL named 'home'
        else:
            # why we use messages.error()?
            # because we want to display an error message to the user
            messages.error(request, 'Invalid email or password')
            return redirect('login')

    return render(request, 'users/login.html')


# User logout view
def logout(request):
    # why we use auth_logout()?
    # because we want to log the user out
    auth_logout(request)
    # why we use messages.success()?
    # because we want to display a success message to the user
    messages.success(request, 'You have been logged out.')
    return redirect('login')
