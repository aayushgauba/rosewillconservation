from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name = 'dashboard'),
    path('contact', views.contactView, name = 'contactView'),
    path('contact/<int:contact_id>', views.contactDetailView, name = 'contactDetailView'),
    path('contact/delete/<int:contact_id>', views.contactDelete, name = 'contactDelete'),
    path('signin', views.signin, name = 'signin'),
    path('signup', views.signup, name = 'signup'),
    path('signout', views.signout, name = 'signout'),
    path('image/add',views.upload, name ="upload"),
    path('image/delete/<int:request_id>',views.delete, name ="delete")

]