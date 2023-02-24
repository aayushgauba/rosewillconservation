from django import forms
from .models import Contact, HomeSlider

class ContactForm(forms.Form):
    Name = forms.CharField()
    Email = forms.EmailField()
    Message = forms.CharField(widget=forms.Textarea)

class ImageSliderForm(forms.ModelForm):
    class Meta:
        model = HomeSlider
        fields= ["Image", "Description"]