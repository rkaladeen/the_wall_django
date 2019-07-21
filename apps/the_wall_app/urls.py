from django.urls import path
from . import views

urlpatterns = [
  path('', views.index),
  path('welcome/', views.home),
  path('register/', views.register),
  path('login/', views.login),
  path('logout/', views.logout),
  path('email/', views.email),
  # Wall Paths (Messages)
  path('post_message/', views.post_message),
  path('delete_message/<int:m_id>/', views.delete_message),
  # Wall Paths (Comments)
  path('post_comment/', views.post_comment),
  path('delete_comment/<int:c_id>/', views.delete_comment),
]