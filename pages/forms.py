from django import forms
from .models import Contact, HomeSlider, Campaign
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.phonenumber import PhoneNumber

class OrderForm(forms.Form):
    Name = forms.CharField()
    Email = forms.EmailField()
    Amount = forms.IntegerField()

class ContactForm(forms.Form):
    Name = forms.CharField()
    Email = forms.EmailField()
    Message = forms.CharField(widget=forms.Textarea)
    PhoneNumber = PhoneNumberField()

class ImageSliderForm(forms.ModelForm):
    class Meta:
        model = HomeSlider
        fields= ["Image", "Description"]

class CampaignForm(forms.ModelForm):
    class Meta:
        model = Campaign
        fields = ["Title", "Description", "MinimumAmount", "Image"]
