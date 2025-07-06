from django.contrib import admin
from .models import Ad


class Adadmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(Ad, Adadmin)
