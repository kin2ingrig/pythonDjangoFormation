from django.urls import path
from . import views

urlpatterns = [
    path('', views.animals, name='animal'),
    # path('All/', views.familles, name='famille'),
]