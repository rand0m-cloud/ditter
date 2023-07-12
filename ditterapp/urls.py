from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("api/v1/timeline", views.timeline, name="timeline"),
    path("api/v1/dweet/<uuid:uuid>", views.view_dweet, name="view_dweet"),
    path("api/v1/like/<uuid:uuid>", views.like_dweet, name="like_dweet"),
]
