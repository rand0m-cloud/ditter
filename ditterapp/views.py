from django.template import loader
from django.http import JsonResponse, HttpResponse
from .models import Dweet


# Creates a list of dweets formatted as a dict
def create_timeline():
    dweets = Dweet.objects.all()
    return [dweet.format() for dweet in dweets]

def index(request):
    print(create_timeline())
    template = loader.get_template("ditterapp/index.html")
    return HttpResponse(template.render({"dweets": create_timeline()}))

# /api/v1/timeline
def timeline(request):
    return JsonResponse(create_timeline(), safe=False)


# /api/v1/dweet/<uuid>
def view_dweet(request, uuid):
    dweet = Dweet.objects.get(id=uuid)
    return JsonResponse(dweet.format())
