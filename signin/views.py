from passlib.hash import pbkdf2_sha256

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from signup.models import Users

def is_username_valid(username):
    """Check to see if username is valid."""
    if username:
        return True
    return False

def is_password_valid(password):
    """Check to see if password is valid."""
    if password:
        return True
    return False

def index(request):
    """Function to sign in."""
    if request.method != "POST":
        return HttpResponseBadRequest("Error: Send your data via POST.")
    post = request.POST.dict()
    # Check for data validity.
    if (set(post.keys()) != {"username", "password"}
        or not is_username_valid(post["username"].lower())
        or not is_password_valid(post["password"])
):
        return HttpResponseBadRequest("Error: Your POST data is corrupted.")
    # Get user from database.
    try:
        user = Users.objects.get(username=post["username"].lower())
    except Users.DoesNotExist:
        return HttpResponseForbidden("No such user exists.")
    # Verify password hash.
    if not pbkdf2_sha256.verify(post["password"], user.password_hash):
        return HttpResponseForbidden("Your password is incorrect.")
    # Set username for session.
    request.session['username'] = user.username
    return HttpResponse(
        "Welcome %s!\nYou were registered on %s, and now, on this great day, you have come back!"
        % ( user.name,
            user.date_registered
))
