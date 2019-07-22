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
    request.session['fname'] = check['user'].first_name
    request.session['is_logged_in'] = True
    return redirect('/welcome')
  else:
    request.session["errors"] = check["errors"]
    return redirect('/')

def fname(request):
  context = {"errors": "", "error_type": "fname"}
  error = User.objects.first_name(request.POST['first_name'])
  context['errors'] = error
  return render(request, 'the_wall_app/partials/registration_partials.html', context)

def lname(request):
  context = {"errors": "", "error_type": "lname"}
  error = User.objects.last_name(request.POST['last_name'])
  context['errors'] = error
  return render(request, 'the_wall_app/partials/registration_partials.html', context)

def email(request):
  context = {"errors": {}, "error_type": "email"}
  error = User.objects.email(request.POST['email'])
  context['errors'] = error
  return render(request, 'the_wall_app/partials/registration_partials.html', context)

def pword(request):
  context = {"errors": {}, "error_type": "pword"}
  error = User.objects.pword(request.POST['password'])
  context['errors'] = error
  return render(request, 'the_wall_app/partials/registration_partials.html', context)

def c_pword(request):
  context = {"errors": {}, "error_type": "c_pword"}
  error = User.objects.c_pword(request.POST['password_confirm'], request.POST['password'])
  context['errors'] = error
  return render(request, 'the_wall_app/partials/registration_partials.html', context)

def dob(request):
  context = {"errors": "", "error_type": "dob"}
  error = User.objects.dob(request.POST['dob'])
  context['errors'] = error
  return render(request, 'the_wall_app/partials/registration_partials.html', context)

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
    # message_poster = 
    context = {
      "all_messages": Message.objects.all(),
      "all_comments": Comment.objects.all()
      }
    return render(request, "the_wall_app/home.html", context)
  return redirect('/')

def logout(request):
  request.session.clear()
  request.session['is_logged_in'] = False
  return redirect('/')

 # Wall Functions (MESSAGES)
def post_message(request):
  Message.objects.create(user=User.objects.get(id=request.session['uid']), message=request.POST['message'])
  return redirect("/welcome")

def delete_message(request, m_id):
  message_to_delete = Message.objects.get(id=m_id)
  message_to_delete.delete()
  return redirect("/welcome")

 # Wall Functions (COMMENTS)
def post_comment(request):
  message_commented_id = request.POST['message_id']
  message_commented = Message.objects.get(id=message_commented_id)
  user_commented_id = request.session['uid']
  user_commented = User.objects.get(id=user_commented_id)
  Comment.objects.create(message=message_commented, user=user_commented, comment=request.POST['comment'])
  return redirect("/welcome")

def delete_comment(request, c_id):
  comment_to_delete = Comment.objects.get(id=c_id)
  comment_to_delete.delete()
  return redirect("/welcome")

####### BOOKS ########
def books(request):
  if request.session['is_logged_in']:
    user = User.objects.get(id=request.session['uid'])
    context = { 
      "all_books": Book.objects.all(),
      "user_likes": user.books_liked.values()
      }
    return render(request, "the_wall_app/books.html", context)

  return redirect('/')

def add_book(request):
  user_to_add_book = User.objects.get(id=request.session['uid'])
  Book.objects.create(user=user_to_add_book, title=request.POST['title'], desc=request.POST['desc'])

  book_added = Book.objects.last()
  book_added.likes.add(user_to_add_book)
  
  return redirect("/books")

def delete_book(request, bk_id):
  book_delete = Book.objects.get(id=bk_id)
  book_delete.delete()
  return redirect("/books")

 # Book Functions View or Edit
def book(request, bk_id):
  if request.session['is_logged_in']: 
    context = { "book": Book.objects.get(id=bk_id) }
    if request.session['uid'] == context['book'].user.id:
      return render(request, "the_wall_app/book_edit.html", context)
    else:
      return render(request, "the_wall_app/book_details.html", context)
  return redirect("/")

  # Fav and Unfav
def fav(request, bk_id):
  user_to_fav = User.objects.get(id=request.session['uid'])
  book_faved = Book.objects.get(id=bk_id)
  book_faved.likes.add(user_to_fav)
  return redirect("/books")

def unfav(request, bk_id):
  user_to_unfav = User.objects.get(id=request.session['uid'])
  book_unfaved = Book.objects.get(id=bk_id)
  book_unfaved.likes.remove(user_to_unfav)
  return redirect("/books")