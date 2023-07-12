from django.shortcuts import render
from django.template import loader
from django.http import JsonResponse, HttpResponse
from django.db.models import F
from .models import Dweet


# Creates a list of dweets formatted as a dict
def create_timeline():
    dweets = Dweet.objects.all()
    return [dweet.format() for dweet in dweets]

def index(request):
    return render(request, "ditterapp/index.html", {"dweets":create_timeline()})

# /api/v1/timeline
def timeline(request):
    return JsonResponse(create_timeline(), safe=False)


# /api/v1/dweet/<uuid>
def view_dweet(request, uuid):
    dweet = Dweet.objects.get(id=uuid)
    return JsonResponse(dweet.format())

# /api/v1/like/<uuid>
def like_dweet(request, uuid):
    try:
        if request.method != "POST":
            return JsonResponse({"error": "must be a POST request"})
        dweet = Dweet.objects.get(uuid=uuid)
        dweet.likes=F("likes") + 1
        dweet.save()

        return JsonResponse({"likes": Dweet.objects.get(uuid=uuid).likes})
    except Dweet.DoesNotExist:
        return JsonResponse({"error": "dweet doesn't exist"})
