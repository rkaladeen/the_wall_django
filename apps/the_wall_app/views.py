from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
# Create your views here.

def index(request):
  # request.session["errors"] = {}
  return render(request, "the_wall_app/index.html")

def register(request):
  check = User.objects.register(request.POST)
  print(check)
  if check["is_valid"]:
    request.session["errors"] = {}
    request.session['uid'] = check['user'].id
    return redirect('/welcome')
  else:
    request.session["errors"] = check["errors"]
    return redirect('/')

def login(request):
  check = User.objects.login(request.POST)
  if check["is_valid"]:
    request.session["errors"] = {}
    request.session['uid'] = check['user'].id
    request.session['fname'] = check['user'].first_name
    return redirect('/welcome')
  else:
    request.session["errors"] = check["errors"]
    return redirect('/')

def home(request):
  return render(request, "the_wall_app/home.html")


