from django.contrib import admin
# from django.contrib.gis.admin import OSMGeoAdmin

from .models import Agent
admin.site.register(Agent)

class AgentAdmin(admin.ModelAdmin):
	list_display = ("first_name","last_name","email","location","agency","phone_number")
	search_fields = ("first_name","last_name","phone_number")
	"""docstring fos Agents"""

		
# Register your models here.
