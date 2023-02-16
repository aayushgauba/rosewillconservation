from django.shortcuts import redirect, render
from .forms import ContactForm
from .models import Contact
from datetime import date

def index(request):
    return render(request, "index.html")
def about(request):
    return render(request, "about.html")
def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = request.POST.get('Name')
            email = request.POST.get('Email')
            message = request.POST.get('Message')
            dateform = date.today()
            Contact.objects.create(Name = name, Email = email, Message = message, Date = dateform)
    return render(request, "contact.html", context = {'form':form})
# Create your views here.
