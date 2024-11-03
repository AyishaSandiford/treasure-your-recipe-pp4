from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('dashboard', views.get_dashboard_view, name='dashboard'),
   path('create', views.Create, name='create'),
   path('edit/<recipe_id>' , views.Edit, name='edit'),
   path('delete/<recipe_id>' , views.Delete, name='delete'),
   path('show/<recipe_id>' , views.Show, name='show'),
]
