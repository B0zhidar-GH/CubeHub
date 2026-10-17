from django.contrib import admin
from .models import Solve

# Register your models here.

@admin.register(Solve)
class SolveAdmin(admin.ModelAdmin):
    list_display = ("cuber", "cube", "time", "date_created")