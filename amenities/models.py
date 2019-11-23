from django.db import models

class Amenities(models.Model):
	hospital = models.CharField(max_length = 50)
	school = models.CharField(max_length = 50)
	church = models.CharField(max_length = 50)


# Create your models here.
