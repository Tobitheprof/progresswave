from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import *
from django.core.paginator import *
from django.db.models import Q
import requests
import json




# <--------------------- Auth Views Start ------------------------------> #

@login_required
def home(request):
    return render(request, 'home.html')


@login_required
def profile(request):
    user_profile = Profile.objects.get(owner=request.user)
    context = {
        'user_profile' : user_profile,
        'title' : 'Edit Profile'
    }
    if request.method == "POST":
        phone_number = request.POST['phone_number']
        nationality = request.POST['nationality']
        title = request.POST['title']

        user_profile.phone_number = phone_number
        user_profile.nationality = nationality
        user_profile.title = title

        user_profile.save()
        messages.info(request, "Profile updated successfully")
        return redirect('home')


        
    return render(request, 'profile.html', context)

@login_required
def logout(request):
    auth.logout(request)
    return redirect('login')

@login_required
def tech(request):
    course = Course.objects.filter(category="technology")
    context = {
        'course' : course,
        'title' : 'Technology',
    }
    return render(request, 'category.html', context)

@login_required
def law(request):
    course = Course.objects.filter(category="technology")
    context = {
        'course' : course,
        'title' : 'Law'
    }
    return render(request, 'category.html', context)


@login_required
def earth(request):
    course = Course.objects.filter(category="earth")
    context = {
        'course' : course,
        'title' : 'Protecting the Earth'
    }
    return render(request, 'category.html', context)


@login_required
def business(request):
    course = Course.objects.filter(category="business")
    context = {
        'course' : course,
        'title' : 'Business'
    }
    return render(request, 'category.html', context)


@login_required
def health(request):
    course = Course.objects.filter(category="health")
    context = {
        'course' : course,
        'title' : 'Health'
    }
    return render(request, 'category.html', context)


@login_required
def nationalism(request):
    course = Course.objects.filter(category="nationalism")
    context = {
        'course' : course,
        'title' : 'Nationalism'
    }
    return render(request, 'category.html', context)


@login_required
def marine(request):
    course = Course.objects.filter(category="marine")
    context = {
        'course' : course,
        'title' : 'Marine Life'
    }
    return render(request, 'category.html', context)

@login_required
def det(request, slug):
    course = Course.objects.get(slug = slug)
    serial_number = request.GET.get('lecture')
    lectures = course.lecture_set.all().order_by('serial_number')


    if serial_number is None:
        serial_number = 1
    lecture = Lecture.objects.get(serial_number = serial_number, course = course)



    context = {
        'course' : course,
        'lecture' : lecture,
        'lectures' : lectures,
        'title' : course

    }
    return render(request, 'det.html', context)

def library(request):
    return render(request, 'library.html')






# <--------------------- Auth Views End ------------------------------> #





# <--------------------- Unauth Views Start ------------------------------> #

def index(request):
    return render(request, 'index.html')

def login(request):
    user = request.user

    if user.is_authenticated:
        return redirect('home')

    context = {
        'title' : 'Login',
    }
    if request.method == 'POST':
        username = request.POST['username'] #Requesting Username
        password = request.POST['password'] #Requesting Password
    
        user = auth.authenticate(username=username, password=password)

        if user is not None: #Cheking If User Exists in the database
            auth.login(request, user) # Logs in User
            return redirect('home') # Redirects to home view
        else:
            messages.info(request, 'Invalid Username or Password') #Conditional Checking if credentials are correct
            return redirect('login')#Redirects to login if invalid

    else:
        return render(request, 'login.html', context)


def register(request):
    context = {
        'title' : 'Sign Up',
    }
    if request.method == 'POST':
        #Requesting POST data
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        #End of POST data request

        #Condition is executed if both passwords are the same
        if password == password2:
            if User.objects.filter(email=email).exists(): #Checking databse for existing data
                messages.info(request, "This email is already in use")#Returns Error Message
                return redirect(register)
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect('register')
            #Else condition executed if the above conditions are not fulfilled    
            else:
                ctx = {
                    'user' : username
                }
                message = get_template('mail.html').render(ctx)
                msg = EmailMessage(
                    'Welcome to ProgressWave',
                    message,
                    'Paradoxx',
                    [email],
                )
                msg.content_subtype ="html"# Main content is now text/html
                msg.send()
                user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name )
                user.save()
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)#Logs in USER



            #Create user model and redirect to edit-profile
            return redirect('cont')#Rediects to specified page once condition is met
        else:
            messages.info(request, "Passwords do not match")
            return redirect("register")
    return render(request, 'register.html', context)

@login_required
def cont(request):
    if Profile.objects.filter(owner=request.user).exists():
        return redirect("home")
    else:
        user_model = User.objects.get(username=request.user)
        new_profile = Profile.objects.create(owner=user_model, id_user=user_model.id)
        new_profile.save()
        ctx = {
            'user' : user_model.username
        }
        message = get_template('mail.html').render(ctx)
        msg = EmailMessage(
            'Welcome to ProgressWave',
            message,
            'ProgressWave',
            [user_model.email],
        )
        msg.content_subtype ="html"# Main content is now text/html
        msg.send()
    return render(request, 'next.html')



# <--------------------- Unauth Views End ------------------------------> #


# Create your views here.
