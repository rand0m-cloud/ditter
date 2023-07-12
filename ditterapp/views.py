from django.http import JsonResponse
from .models import Dweet


def index(request):
    return timeline(request)


def timeline(request):
    dweets = Dweet.objects.all()

    resp = [dweet.format() for dweet in dweets]
    return JsonResponse(resp, safe=False)


def view_dweet(request, uuid):
    dweet = Dweet.objects.get(id=uuid)
    return JsonResponse(dweet.format())
