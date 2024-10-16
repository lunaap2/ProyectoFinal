from django.urls import path
from . import views


urlpatterns = [
    path('servicios/', views.servicios),
    path('', views.inicio) 
]

