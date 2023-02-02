from django.urls import path
from . import views

urlpatterns = [
    path('', views.animals, name='animals'),
    path('familles', views.familles, name='familles'),
]