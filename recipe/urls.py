from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('dashboard', views.get_dashboard_view, name='dashboard'),
]
