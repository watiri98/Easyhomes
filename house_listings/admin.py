from django.contrib import admin

from .models import House_listings
admin.site.register(House_listings)

class House_listingsAdmin(admin.ModelAdmin):
	list_display = ("Location","Category","Bedrooms","Bathrooms","Amenities")
	search_fields = ("Location","Category")

# Register your models here.
