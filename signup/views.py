import datetime
from passlib.hash import pbkdf2_sha256

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest

from signup.models import Users


def is_username_valid(username):
    """Check to see if username is valid."""
    if (3 <= len(username) <= 100
        and username.replace('_', '').isalnum()
        and (username[0].isalpha() or username[0] == '_')
):
        return True
    return False

def is_password_valid(password):
    """Check to see if password is valid."""
    if len(password) >= 8:
        return True
    return False

def is_name_valid(name):
    """Check to see if name is valid."""
    if 0 <= len(name) <= 100:
        return True
    return False

def index(request):
    """Sign up on the site."""
    if request.method != "POST":
        return HttpResponseBadRequest("Error: Send your data via POST.")
    post = request.POST.dict()
    # Check for data validity.
    if (set(post.keys()) != {"name", "username", "password"} 
        or not is_name_valid(post["name"])
        or not is_username_valid(post["username"].lower())
        or not is_password_valid(post["password"])
):
        return HttpResponseBadRequest("Error: Your POST data is corrupted.")
    # Check to see if username exists.
    if Users.objects.filter(username=post["username"].lower()):
        return HttpResponseBadRequest("This username already exists.")
    # Hash password.
    password_hash = pbkdf2_sha256.encrypt(post['password'],
                                          rounds=100000,
                                          salt_size=16)
    date = str(datetime.datetime.now().ctime())
    # Create user.
    Users.objects.create(name=post['name'],
                         username=post['username'].lower(),
                         password_hash=password_hash,
                         date_registered=date)
    return HttpResponse("Registration has been completed.")
