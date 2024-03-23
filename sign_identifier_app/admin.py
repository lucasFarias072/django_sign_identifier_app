

from django.contrib import admin
from .models import *


@admin.register(Sign)
class SignAdmin(admin.ModelAdmin):
    list_display = ('birthday', 'created', 'updated', 'availability')


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender')
