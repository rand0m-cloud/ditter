from django.shortcuts import render
from django.template import loader
from django.http import JsonResponse, HttpResponse
from django.db.models import F
from django.contrib.auth import authenticate, login
from django.contrib.sessions.backends.db import SessionStore
from django.db.utils import IntegrityError
import json

from .models import Dweet, DweetLike, Author


# Creates a list of dweets formatted as a dict
def create_timeline(request):
    dweets = [dweet.format() for dweet in Dweet.objects.all()]
    for dweet in dweets:
        likes = [
            like.user.username
            for like in DweetLike.objects.filter(dweet_id=dweet["uuid"])
        ]
        dweet["liked_by"] = likes

    return dweets


# GET /api/v1/timeline
def timeline(request):
    return JsonResponse(create_timeline(request), safe=False)


# GET /api/v1/dweet/<uuid>
def view_dweet(request, uuid):
    dweet = Dweet.objects.get(id=uuid)
    return JsonResponse(dweet.format())


# POST /api/v1/like/<uuid>
def like_dweet(request, uuid):
    try:
        if request.method != "POST":
            return JsonResponse({"error": "must be a POST request"})

        request_json = json.loads(request.body)
        session = SessionStore(session_key=request_json["session"])

        if "uuid" not in session:
            return JsonResponse({"error": "please login first"})

        author = Author.objects.get(uuid=session["uuid"])

        like = DweetLike(dweet=Dweet.objects.get(uuid=uuid), user=author)
        like.save()

        return JsonResponse({})
    except IntegrityError:
        return JsonResponse({"error": "already liked this tweet"})
    except Dweet.DoesNotExist:
        return JsonResponse({"error": "dweet doesn't exist"})


# POST /api/v1/login
def login_view(request):
    if request.method != "POST":
        return JsonResponse({"error": "must be a POST request"})

    login_json = json.loads(request.body)

    if "username" not in login_json or "password" not in login_json:
        return JsonResponse({"error": "Missing username or password"})

    user = authenticate(
        request, username=login_json["username"], password=login_json["password"]
    )
    if user is None:
        return JsonResponse({"error": "Wrong username or password"})

    login(request, user)

    author = Author.objects.get(user=user)
    request.session["uuid"] = str(author.uuid)

    author_json = author.format()
    author_json["session"] = request.session.session_key
    return JsonResponse(author_json)
