from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed

# Create your views here.

def is_username_valid(username):
    if len(username) >= 3 and username.replace('_', '').isalnum() and (username[0].isalpha() or username[0] == '_'):
        return True
    return False

def is_password_valid(password):
    if len(password) >= 8:
        return True
    return False

def is_name_valid(name):
    if name:
        return True
    return False

def index(request):
    if request.method != "POST":
        return HttpResponse("Error: Send your data via POST.")
    post = request.POST.dict()
    if (set(post.keys()) != {'name', 'username', 'password'} 
        or not is_name_valid(post['name'])
        or not is_username_valid(post['username'])
        or not is_password_valid(post['password'])
):
        return HttpResponse("Error: Your POST data is corrupted.\n")
    return HttpResponse(str(post))
