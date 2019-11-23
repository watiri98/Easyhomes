
from django.db import models
from agent.models import Agent


class Client(models.Model):
	first_name = models.CharField(max_length = 50)
	last_name = models.CharField(max_length = 50)
	email = models.EmailField(max_length=100)
	phone_number = models.CharField(max_length=15)
	# house_description = models.TextField()
	registration_no = models.CharField(max_length=20)
	agent = models.ForeignKey("agent.Agent", on_delete=models.CASCADE)



	def __str__(self):
		return self.registration_no

# Create your models here.

# clients login
# dashboard
# SEARCH HOUSES
