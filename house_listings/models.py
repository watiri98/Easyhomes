from django.db import models
from amenities.models import Amenities

class House_listings(models.Model):
	Location = models.CharField(max_length = 50)
	Category = (('apartment'),('flat'))
	Bedrooms = [('bedsitter'),('1bedroom'),('2bedroom'),('3bedroom')]
	Bathrooms = [('1'),('2'),('3')]
	Amenities = models.ForeignKey("amenities.Amenities", on_delete=models.CASCADE)

	
