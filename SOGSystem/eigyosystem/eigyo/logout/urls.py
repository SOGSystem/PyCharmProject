from django.urls import path, include
from eigyosystem.eigyo.logout import views

urlpatterns = [
    path('', views.logouteigyo, name='logouteigyo'),  # index
]