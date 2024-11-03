from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('dashboard', views.get_dashboard_view, name='dashboard'),
   path('create', views.Create, name='create'),
   path('edit/<recipe_id>' , views.Edit, name='edit'),
]
