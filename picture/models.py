from django.db import models

class Picture(models.Model):
	number_of_rooms = models.CharField(max_length = 10)
	image = models.FileField(upload_to="images", blank = True) 


	def __str__(self):
		return self.image()

	# def __str__(self):
	# 	return self.listings()



# Create your models here.
