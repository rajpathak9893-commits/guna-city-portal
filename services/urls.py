from django.urls import path
from . import views

urlpatterns = [
    path('',        views.services_list,  name='services'),
    path('add/',    views.add_service,    name='add_service'),
    path('<int:id>/', views.service_detail, name='service_detail'),
]