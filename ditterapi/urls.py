from django.urls import path

from . import views

urlpatterns = [
    path("timeline", views.timeline, name="timeline"),
    path("dweet/<uuid:uuid>", views.view_dweet, name="view_dweet"),
    path("like/<uuid:uuid>", views.like_dweet, name="like_dweet"),
    path("login", views.login_view, name="login_view"),
    path("dweet", views.post_dweet, name="post_dweet"),
]
