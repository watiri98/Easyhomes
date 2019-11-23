from django.urls import path
from .views import add_agent
from .views import list_agents


urlpatterns = [
path("add/",add_agent,name = "add_agent"),
path("list/",list_agents, name = "list_agents")




]