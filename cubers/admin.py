from django.contrib import admin
from .models import Cuber

# Register your models here.

@admin.register(Cuber)
class CuberAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "country", "favourite_cube")