from django.db import models
from datetime import datetime, date
import re, bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
  def register(self, postData):
    valid = {
      "is_valid": True,
      "user": None,
      "errors": {}
    }
    
    #validations
    if len(postData['first_name'])<1:
      valid['errors']['first_name'] = "First name is required!"
    elif len(postData['first_name'])<2:
      valid['errors']['first_name'] = "First name must be at least 2 characters!"
    if len(postData['last_name'])<1:
      valid['errors']['last_name'] = "Last name is required!"
    elif len(postData['last_name'])<2:
      valid['errors']['last_name'] = "Last name must be at least 2 characters!"
    if len(postData['email'])<1:
      valid['errors']['email'] = "Email is required!"
    elif not EMAIL_REGEX.match(postData['email']):
      valid['errors']['email'] = "Invalid email!"
    else:
      valid['user'] = User.objects.filter(email=postData['email'].lower())
      if len(valid['user']) > 0:
          valid['errors']['email'] = "Email already exists!"
   
   
    if len(postData['password'])<1:
      valid['errors']['password'] = "Password is required!"
    elif len(postData['password'])<8:
      valid['errors']['password'] = "Password must be at least 8 characters!"
    if len(postData['password_confirm'])<1:
      valid['errors']['password_confirm'] = "Password confirm is required!"
    elif postData['password'] != postData['password_confirm']:
      valid['errors']['password_confirm'] = "Passwords must match!"
    if len(postData['dob']) < 1:
      valid['errors']['dob'] = "Date of Birth is required!"
    else:
      dob = datetime.strptime(postData['dob'], "%Y-%m-%d")
      if dob > datetime.now():
        valid['errors']['dob'] = "Date of Birth must be in the past"       
      else:
        today = date.today() 
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day)) 
        if age < 13:
          valid['errors']['dob'] = "You must be at least 13 to register"      
    if len(postData['gender']) < 1:
      valid['errors']['gender'] = "Please select a gender"

    if len(valid['errors']) == 0:
      valid["user"] = User.objects.create(
          first_name=postData["first_name"],
          last_name=postData["last_name"],
          email=postData["email"].lower(),
          password=bcrypt.hashpw(postData["password"].encode(), bcrypt.gensalt()).decode(),
          dob=postData["dob"],
          gender=postData["gender"])
    else:
      valid["is_valid"] = False
    return valid
  
  def login(self, postData):
    valid= {
        "is_valid": True,
        "user": None,
        "errors": {}
    }
    # validations
    if len(postData['login_email'])<1:
      valid['errors']['login_email'] = "Email is required!"
    elif not EMAIL_REGEX.match(postData['login_email']):
      valid['errors']['login_email'] = "invalid email!"
    else:
      valid['user'] = User.objects.filter(email=postData['login_email'].lower())
      if len(valid['user']) == 0:
        valid['errors']['login_email'] = "unknown email"
    if len(postData['login_password'])<1:
      valid['errors']['login_password'] = "Password is required!"
    elif len(postData['login_password'])<8:
      valid['errors']['login_password'] = "Password must be at least 8 characters!"
    if len(valid['errors']) == 0:
      valid['user'] = valid['user'][0]

      check = bcrypt.checkpw(postData['login_password'].encode(), valid['user'].password.encode())
      if not check:
        valid["is_valid"] = False
        valid["errors"]["login_password"] = "Invalid login information."
    
    if len(valid['errors']) == 0:
      valid["is_valid"] = True
      return valid
    valid["is_valid"] = False

    return valid

class User(models.Model):
  # id auto-generated
  first_name = models.CharField(max_length=45)
  last_name = models.CharField(max_length=45)
  email = models.CharField(max_length=45)
  password = models.CharField(max_length=255)
  dob = models.DateField(null=True)
  gender = models.CharField(max_length=10)
  user_level = models.CharField(max_length=45, default="user")
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  # comments attribute added
  objects = UserManager()

class Message(models.Model):
  # id auto-generated
  user = models.ForeignKey(User, related_name="messages", on_delete=models.CASCADE)
  message = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  # comments attribute added

class Comment(models.Model):
  # id auto-generated
  message = models.ForeignKey(Message, related_name="comments", on_delete=models.CASCADE)
  user = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
  comment = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)