from passlib.hash import pbkdf2_sha256

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from signup.models import Users

def is_username_valid(username):
    if username:
        return True
    return False

def is_password_valid(password):
    if password:
        return True
    return False

def index(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Error: Send your data via POST.")
    post = request.POST.dict()
    if (set(post.keys()) != {"username", "password"}
        or not is_username_valid(post["username"])
        or not is_password_valid(post["password"])
):
        return HttpResponseBadRequest("Error: Your POST data is corrupted.")
    try:
        user = Users.objects.get(username=post["username"])
    except Users.DoesNotExist:
        return HttpResponseForbidden("No such user exists.")
    if not pbkdf2_sha256.verify(post["password"], user.password_hash):
        return HttpResponseForbidden("Your password is incorrect.")
    return HttpResponse(
        "Welcome %s!\nYou were registered on %s, and now, on this great day, you have come back!"
        % ( user.name,
            user.date_registered
))
