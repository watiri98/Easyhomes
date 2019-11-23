from django.urls import path
from .views import add_client


urlpatterns = [
path("add/",add_client,name = "add_client"),
