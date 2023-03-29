from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name = 'dashboard'),
    path('campaigns', views.campaignsView, name='campaignsView'),
    path('campaigns/add', views.campaignAdd, name='campaignAdd'),
    path('campaigns/update/<int:campaign_id>', views.campaignUpdate, name='campaignUpdate'),
    path('contact', views.contactView, name = 'contactView'),
    path('contact/<int:contact_id>', views.contactDetailView, name = 'contactDetailView'),
    path('contact/delete/<int:contact_id>', views.contactDelete, name = 'contactDelete'),
    path('signin', views.signin, name = 'signin'),
    path('signup', views.signup, name = 'signup'),
    path('signout', views.signout, name = 'signout'),
    path('image/add',views.upload, name ="upload"),
    path('search', views.search, name = "search"),
    path('image/delete/<int:request_id>',views.delete, name ="delete"),
]