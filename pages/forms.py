from django import forms
from .models import Contact

class ContactForm(forms.Form):
    Name = forms.CharField()
    Email = forms.EmailField()
    Message = forms.CharField(widget=forms.Textarea)
