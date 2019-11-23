from django.contrib import admin

from .models import Picture

class PictureAdmin(admin.ModelAdmin):
	list_display = ("number_of_rooms","image")
	search_fields = ("number_of_rooms")

# Register your models here.
