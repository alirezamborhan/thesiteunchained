from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseBadRequest
from signup.models import Users

def index(request):
    if request.session.has_key("username"):
        username = request.session["username"]
        user = Users.objects.get(username=username)
        return HttpResponse("This is your dummy page, %s! Enjoy it." % user.name)
    else:
        return HttpResponseForbidden("Error: You are not logged in.")

def signout(request):
    if request.session.has_key("username"):
        user = Users.objects.get(username=request.session['username'])
        del request.session['username']
        return HttpResponse("You are logged out, %s! See you later." % user.name)
    else:
        return HttpResponseBadRequest("Error: You are not logged in.")
