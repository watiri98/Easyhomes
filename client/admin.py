from django.contrib import admin
# from django.contrib.gis.admin import OSMGeoAdmin

from .models import Client
admin.site.register(Client)

class ClientAdmin(admin.ModelAdmin):
	list_display = ("first_name","last_name","email","location","type_of_house","phone_number")
	search_fields = ("first_name","last_name","phone_number")

