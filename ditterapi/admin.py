from django.contrib import admin
from .models import Author, Dweet, DweetLike

admin.site.register(Author)
admin.site.register(Dweet)
admin.site.register(DweetLike)
