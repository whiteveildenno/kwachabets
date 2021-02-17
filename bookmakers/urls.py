from django.urls import path

from . import views

urlpatterns = [
  path('bookie', views.bookie, name ='bookie'),
]