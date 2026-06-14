from django.urls import path
from . import views

urlpatterns = [

    path('', views.education_list, name='education_list'),

    path('add/', views.add_education, name='add_education'),

    path('schools/', views.schools_list, name='schools'),

    path('colleges/', views.colleges_list, name='colleges'),

    path('coaching/', views.coaching_list, name='coaching'),

]