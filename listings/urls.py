# businesses/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.listings_home, name='listings_home'),
    path('add/', views.add_listing, name='add_listing'),
    path('<slug:slug>/', views.listing_detail, name='listing_detail'),
    path('<slug:slug>/edit/', views.edit_listing, name='edit_listing'),
    path('<slug:slug>/delete/', views.delete_listing, name='delete_listing'),
]