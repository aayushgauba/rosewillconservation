from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('about', views.about, name = 'about'),
    path('contact', views.contact, name = 'contact'),
    path('contact/post/<int:contact_id>', views.contactpost, name = 'contactpost'),
    path('donate', views.donate, name = 'donate'),
]