from django.contrib import admin

from .models import Amenities
admin.site.register(Amenities)

class AmenitiesAdmin(admin.ModelAdmin):
	list_display = ("hospital","school","church")
	search_fields = ("hospital")

# Register your models here.
