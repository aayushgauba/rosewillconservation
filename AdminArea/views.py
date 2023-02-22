from django.shortcuts import render
from django.contrib import messages,auth,admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.shortcuts import render, redirect
import re
# Create your views here.
def isValidEmail(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if(re.fullmatch(regex, email)):
        return True
    else:
        return False

def dashboard(request):
    if(request.user.is_authenticated):
        return render(request, 'admin/dashboard.html')
    else:
        return redirect('signin')
    
def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            user = auth.authenticate(username=email, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid Credentials')
                return redirect('signin')
    else:    
        return render(request, 'admin/signin.html')

def signup(request):
    user = User.objects.all()
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        passwordcheck = request.POST.get('password2')

        if(password != passwordcheck):
            messages.error(request, 'Passswords dont match')
            return redirect(signup)
        if(user.filter(username = username).count() != 0):
            messages.error(request, 'Username already exists')
            return redirect(signup)
        if(isValidEmail(email) == False):
            messages.error(request, 'Please enter a valid email')
            return redirect(signup)
        if(firstname == ""):
            messages.error(request, 'Please enter a First Name')
            return redirect(signup)
        if(lastname == ""):
            messages.error(request, 'Please enter a Last Name')
            return redirect(signup)
        if(username == ""):
            messages.error(request, 'Please enter a Username')
            return redirect(signup)

        else:
            User.objects.create_user(username = username, first_name = firstname, email = email, last_name = lastname, password=password, is_staff=False, is_superuser = True)
            return redirect('signin')

    return render(request, 'admin/signup.html')

def signout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request,'You are now logged out')
        return redirect('index')