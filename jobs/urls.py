from django.urls import path
from . import views

urlpatterns = [
    path('', views.jobs_list, name='jobs'),
    path('add/', views.add_job, name='add_job'),
    path('<int:id>/', views.job_detail, name='job_detail'),
]