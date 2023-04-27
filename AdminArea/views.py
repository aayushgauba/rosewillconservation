from django.shortcuts import render
from django.contrib import messages,auth,admin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.shortcuts import render, redirect
import re
from pages.models import Contact, HomeSlider, Campaign, Order
from pages.forms import ImageSliderForm, CampaignForm
from .forms import Userform
from django.conf import settings
from decimal import Decimal
from paypal.standard.forms import PayPalPaymentsForm
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse

def isValidEmail(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if(re.fullmatch(regex, email)):
        return True
    else:
        return False

def dashboard(request):
    if(request.user.is_authenticated):
        images = HomeSlider.objects.all()
        return render(request, 'admin/dashboard.html', context={'images':images})
    else:
        return redirect('signin')

def contactView(request):
    if(request.user.is_authenticated):
        contacts = Contact.objects.all()
        return render(request, 'admin/contactView.html', context={'contacts':contacts})
    else:
        return redirect('signin')

def contactDetailView(request, contact_id):
    if(request.user.is_authenticated):
        contact = Contact.objects.get(id = contact_id)
        return render(request, 'admin/contactDetailView.html', context={'contact':contact})
    else:
        return redirect('signin')

def contactDelete(request, contact_id):
    if request.method == "POST":
        contact = Contact.objects.get(id = contact_id)
        contact.delete()
        return redirect('contactView')

def campaignsView(request):
    campaigns = Campaign.objects.all()
    return render(request, 'admin/campaignView.html', context={"campaigns":campaigns})

def signin(request):
    if request.method == 'POST':
        emailuser = request.POST.get('email')
        passworduser = request.POST.get('password')
        user = auth.authenticate(username = emailuser,password = passworduser)

        if user is not None:
            auth.login(request, user)
            return redirect('contactView')
        else:
            return redirect('signin')
    else:    
        return render(request, 'admin/signin.html')

def upload(request):
    if request.method == 'POST':
        form = ImageSliderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ImageSliderForm()
    context = {
            'form':form,
        }
    return render(request, 'admin/imageSliderAdd.html', context)

def campaignAdd(request):
    if request.method == 'POST':
        form = CampaignForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('campaignsView')
    else:
        form = CampaignForm()
    context = {
            'form':form,
        }
    return render(request, 'admin/campaignAdd.html', context)    

def campaignUpdate(request, campaign_id):
    campaign = Campaign.objects.get(id=campaign_id)
    if request.method == 'POST':
        form = CampaignForm(request.POST, request.FILES, instance=campaign)
        if form.is_valid():
            form.save()
            return redirect('campaignsView')
    else:
        form = CampaignForm(instance=campaign)
    context = {
            'form':form,
        }
    return render(request, 'admin/campaignAdd.html', context)

def campaignDelete(request, campaign_id):
    if request.method == 'POST':
        campaign = Campaign.objects.get(id = campaign_id)
        campaign.delete()
        return redirect('campaignsView')

def campaignView(request, campaign_id):
    campaign = Campaign.objects.get(id = campaign_id)
    return render(request, 'admin/campaignDetailView.html', context={"campaign":campaign})

def delete(request, request_id):
    if request.method == 'POST':
        image = HomeSlider.objects.get(id = request_id)
        image.delete()
        return redirect('dashboard')

def signup(request):
    form = Userform()
    if request.method == 'POST':
        if form.is_valid():
            form.submit()
        else:
            return redirect('signup')

    return render(request, 'admin/register.html', context = {"form":form})

def search(request):
    if request.method == "POST":
        query = request.POST.get("query")
        contacts = Contact.objects.filter(Name__contains = query)
        if(contacts.count() == 0):
            contacts = Contact.objects.filter(Email__contains=query)
        if(contacts.count() == 0):
            contacts = Contact.objects.filter(Message__contains=query)
        
        images = HomeSlider.objects.filter(Description__contains = query)
        campaigns = Campaign.objects.filter(Title__contains = query)
        if(campaigns.count() == 0):
            campaigns.filter(Description__contains= query)
        return render(request, "Admin/adminSearch.html", context={"contacts":contacts, "images":images, "campaigns":campaigns, "query":query})


def signout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request,'You are now logged out')
        return redirect('index')

