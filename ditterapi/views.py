from django.core.exceptions import ValidationError
from django.shortcuts import render
from django.template import loader
from django.http import JsonResponse, HttpResponse
from django.db.models import F
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.password_validation import validate_password
from django.contrib.sessions.backends.db import SessionStore
from django.db.utils import IntegrityError
from django.core.validators import RegexValidator
import json
import functools

from .models import Dweet, DweetLike, Author, InviteCode


# checks if request is a post and returns an error if not
def is_post(f):
    @functools.wraps(f)
    def inner(request, *args, **kwargs):
        if request.method != "POST":
            return JsonResponse({"error": "must be a POST request"})
        return f(request, *args, **kwargs)

    return inner


# checks if request is a post with session data in the body
# calls the inner function with the session object
def is_logged_in(f):
    @is_post
    @functools.wraps(f)
    def inner(request, *args, **kwargs):
        request_json = json.loads(request.body)
        session_token = None

        try:
            session_token = request_json["session"]
        except IndexError:
            return JsonResponse({"error": "missing session token; please login first"})

        session = SessionStore(session_key=session_token)

        if "uuid" not in session:
            return JsonResponse({"error": "please login first"})

        return f(request, session, *args, **kwargs)

    return inner


# creates a list of dweets formatted as a dict
def create_timeline(request):
    dweets = [dweet.format() for dweet in Dweet.objects.all().order_by("-created_on")]
    return dweets


# GET /api/v1/timeline
def timeline(request):
    return JsonResponse(create_timeline(request), safe=False)


# GET /api/v1/dweet/<uuid>
def view_dweet(request, uuid):
    dweet = Dweet.objects.get(uuid=uuid)
    return JsonResponse(dweet.format())


# POST /api/v1/like/<uuid>
@is_logged_in
def like_dweet(request, session, uuid):
    try:
        author = Author.objects.get(uuid=session["uuid"])

        like = DweetLike(dweet=Dweet.objects.get(uuid=uuid), user=author)
        like.save()

        return JsonResponse({})
    except IntegrityError:
        return JsonResponse({"error": "already liked this tweet"})
    except Dweet.DoesNotExist:
        return JsonResponse({"error": "dweet doesn't exist"})


# POST /api/v1/dweet
@is_logged_in
def post_dweet(request, session):
    request_json = json.loads(request.body)
    dweet = Dweet(author_id=session["uuid"], content=request_json["content"])
    dweet.save()
    return JsonResponse({"uuid": dweet.uuid})


# POST /api/v1/login
@is_post
def login_view(request):
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


# GET /api/v1/user/<username>
def get_user_profile(request, username):
    try:
        author = Author.objects.get(username=username)
        dweets = Dweet.objects.filter(author=author)
        return JsonResponse(
            {"author": author.format(), "dweets": [dweet.format() for dweet in dweets]}
        )
    except Author.DoesNotExist:
        return JsonResponse({"error": "Uh Oh! This user does not exist."})


# POST /api/v1/register
@is_post
def register_user(request):
    try:
        request_json = json.loads(request.body)
        display_name = request_json["display_name"]
        username = request_json["username"]
        password = request_json["password"]
        invite_code = request_json["invite_code"]

        RegexValidator(
            "^[\\dA-z]{3,50}$",
            message="Usernames can only be a combination of characters, numbers, and underscores.\n Usernames must be between 3 and 50 characters in length",
        )(username)
        RegexValidator(
            "^.{2,50}$",
            message="Display names have to between 2 and 50 characters in length",
        )(display_name)
        validate_password(password)

        code = InviteCode.objects.get(code=invite_code)
        user = get_user_model().objects.create_user(username, password=password)
        author = Author.objects.create(
            user=user,
            username=username,
            display_name=display_name,
        )

        code.delete()
        user.save()
        author.save()

        return JsonResponse({})
    except KeyError:
        return JsonResponse({"error": "missing a field in this request"})
    except IntegrityError:
        return JsonResponse({"error": "This username is already taken"})
    except ValidationError as e:
        return JsonResponse({"error": e.messages})
    except InviteCode.DoesNotExist:
        return JsonResponse(
            {"error": "Invite code does not exist or has been redeemed"}
        )


@is_post
@is_logged_in
def logout(reqeust, session):
    session.delete()
    return JsonResponse({})
