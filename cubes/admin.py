from django.contrib import admin
from .models import Cube

# Register your models here.

@admin.register(Cube)
class CubeAdmin(admin.ModelAdmin):
    list_display = ("cube", "category_event", "brand")