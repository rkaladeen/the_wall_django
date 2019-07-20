from django.urls import path
from . import views

urlpatterns = [
  path('', views.index),
  path('welcome/', views.home),
  path('register/', views.register),
  path('login/', views.login),
  path('logout/', views.logout),
  path('email/', views.email),
]