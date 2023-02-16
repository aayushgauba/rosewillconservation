from django.shortcuts import redirect, render, redirect
from .forms import ContactForm
from .models import Contact
from datetime import date
import datetime

def index(request):
    yearstring = "© " + str(date.today().year) +" Rosewill Conservation, Inc"
    return render(request, "index.html", context={'year':yearstring})
def about(request):
    yearstring = "© " + str(date.today().year) +" Rosewill Conservation, Inc"
    return render(request, "about.html", context={'year':yearstring})
def contact(request):
    form = ContactForm()
    yearstring = "© " + str(date.today().year) +" Rosewill Conservation, Inc"
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = request.POST.get('Name')
            email = request.POST.get('Email')
            message = request.POST.get('Message')
            dateform = date.today()
            timeStamp = datetime.datetime.now()
            Contact.objects.create(Name = name, Email = email, Message = message, Date = dateform, timeStamp = timeStamp)
            contact = Contact.objects.get(Name = name, Email = email, Date = dateform, timeStamp = timeStamp)
            
            return redirect("contactpost", contact.id)
    return render(request, "contact.html", context = {'form':form, 'year':yearstring})

def contactpost(request, contact_id):
    yearstring = "© " + str(date.today().year) +" Rosewill Conservation, Inc"
    return render(request, "contactsuccess.html", context = {'year':yearstring})
# Create your views here.
