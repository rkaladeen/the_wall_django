from django.urls import path
from . import views

urlpatterns = [
  path('', views.index),
  path('welcome/', views.home),
  path('register/', views.register),
  path('login/', views.login),
  path('logout/', views.logout),
  # AJAX Validation Paths
  path('fname/', views.fname), #Ajax 
  path('lname/', views.lname), #Ajax
  path('email/', views.email), #Ajax 
  path('pword/', views.pword), #Ajax 
  path('c_pword/', views.c_pword), #Ajax 
  path('dob/', views.dob), #Ajax 
  # Wall Paths (Messages)
  path('post_message/', views.post_message),
  path('delete_message/<int:m_id>/', views.delete_message),
  # Wall Paths (Comments)
  path('post_comment/', views.post_comment),
  path('delete_comment/<int:c_id>/', views.delete_comment),
  # Books Paths
  path('books/', views.books),
  path('add_book/', views.add_book),
  path('delete_book/<int:bk_id>/', views.delete_book),
  # Book Path View or Edit
  path('books/<int:bk_id>/', views.book),
  #fav and unfav paths
  path('fav/<int:bk_id>/', views.fav),
  path('unfav/<int:bk_id>/', views.unfav),
]