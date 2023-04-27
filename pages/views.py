from django.shortcuts import redirect, render, redirect
from .forms import ContactForm, OrderForm
from .models import Contact, HomeSlider, Campaign, Order
from datetime import date
import datetime
from django.conf import settings
from decimal import Decimal
from paypal.standard.forms import PayPalPaymentsForm
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse

def index(request):
    images = HomeSlider.objects.all()
    yearstring = "© " + str(date.today().year) +" Rosewill Conservation, Inc"
    return render(request, "index.html", context={'year':yearstring, 'images':images})

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
            phonenumber = request.POST.get('PhoneNumber')
            dateform = date.today()
            timeStamp = datetime.datetime.now()
            Contact.objects.create(Name = name, Email = email, Message = message, PhoneNumber = phonenumber, Date = dateform, timeStamp = timeStamp)
            contact = Contact.objects.get(Name = name, Email = email, Date = dateform, PhoneNumber = phonenumber, timeStamp = timeStamp)
            
            return redirect("contactpost", contact.id)
    return render(request, "contact.html", context = {'form':form, 'year':yearstring})

def contactpost(request, contact_id):
    yearstring = "© " + str(date.today().year) +" Rosewill Conservation, Inc"
    return render(request, "contactsuccess.html", context = {'year':yearstring})

def donate(request):
    yearstring = "© " + str(date.today().year) +" Rosewill Conservation, Inc"
    donations = Campaign.objects.all()
    return render(request, "donate.html", context = {'donations':donations, 'year':yearstring})

def donateView(request, donation_id):
    yearstring = "© " + str(date.today().year) +" Rosewill Conservation, Inc"
    donation = Campaign.objects.get(id = donation_id)
    orderform = OrderForm()
    if(request.method == "POST"):
        orderform = OrderForm(request.POST)
        if orderform.is_valid():
            name = request.POST.get("Name")
            email = request.POST.get("Email")
            amount = request.POST.get("Amount")
            paid = False
            Order.objects.create(Campaign_id = donation_id, Name = name, Email =email, Amount = amount, paid= paid)
            order_id = Order.objects.get(Campaign_id = donation_id, Name = name, Email =email, Amount = amount, paid= paid).id
            return redirect("processPayment", donation_id, order_id)
    return render(request, "donateDetailView.html", context = {'donation':donation, 'year':yearstring, 'form':orderform})

@csrf_exempt
def paymentDoneRedirect(order_id):
    order = Order.objects.get(id = order_id)
    order.paid = True
    order.save()
    return redirect("paymentDone")

@csrf_exempt
def paymentDone(request):
    return render(request, "donateConfirm.html")

def processPayment(request, donation_id, order_id):
    order = Order.objects.get(id=order_id)
    host = request.get_host()

    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': '%.2f' % order.Amount,
        'item_name': 'Order {}'.format(order.id),
        'invoice': str(order.id),
        'currency_code': 'USD',
        'notify_url': 'http://{}{}'.format(host,
                                           reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format(host,
                                           reverse('paymentDoneRedirect', kwargs={"order_id":order_id})),
        'cancel_return': 'http://{}{}'.format(host,
                                              reverse('donate')),
    }

    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'donatePaypal.html', {'order': order, 'form': form})

