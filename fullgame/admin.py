from django.contrib import admin
from .models import Players, Teams, SavedGame

# Register your models here.

admin.site.register(Players)
admin.site.register(Teams)
admin.site.register(SavedGame)