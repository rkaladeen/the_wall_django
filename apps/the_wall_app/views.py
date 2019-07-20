from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
# Create your views here.

def index(request):
  # request.session["errors"] = {}
  
  return render(request, "the_wall_app/index.html")

def register(request):
  check = User.objects.register(request.POST)
  request.session["reg_info"] = {
          "first_name": request.POST["first_name"],
          "last_name": request.POST["last_name"],
          "email": request.POST["email"].lower()
          }
  # print(check)
  if check["is_valid"]:
    request.session["errors"] = {}
    request.session['uid'] = check['user'].id
    request.session['is_logged_in'] = True
    return redirect('/welcome')
  else:
    request.session["errors"] = check["errors"]
    return redirect('/')

def email(request):
  context = {"found": False}
  check = User.objects.filter(email=request.POST['email'])
  new = check.values()
  if new.exists():
    context['found'] = True
  # print("EMAIL FUNCTION FOUND", context['found'])
  # print("EMAIL FUNCTION VALUE", new.exists())
  return render(request, 'the_wall_app/partials/email.html', context)

def login(request):
  request.session["reg_info"] = {} #Once user is logged in stored reg details is cleared
  check = User.objects.login(request.POST)
  if check["is_valid"]:
    request.session["errors"] = {}
    request.session['uid'] = check['user'].id
    request.session['fname'] = check['user'].first_name
    request.session['is_logged_in'] = True
    return redirect('/welcome')
  else:
    request.session["errors"] = check["errors"]
    return redirect('/')

def home(request):
  if request.session['is_logged_in']:
    return render(request, "the_wall_app/home.html")
  return redirect('/')

def logout(request):
  request.session.clear()
  request.session['is_logged_in'] = False
  return redirect('/')

