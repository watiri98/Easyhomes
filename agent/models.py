from django.db import models


class Agent(models.Model):
	First_name = models.CharField(max_length = 50)
	Last_name = models.CharField(max_length = 50)
	Email = models.EmailField()
	Gender = models.CharField(max_length = 20)
	Phone_number = models.CharField(max_length = 15)
	Agency_name = models.CharField(max_length = 50)
	
	Description = models.CharField(max_length = 100)
	Reg_no = models.CharField(max_length = 15)


	def __str__(self):
		return self.First_name + " " + self.Last_name

# Create your models here.

# #agent details
# |
# #house details
# |
# #imaages
# |

# #clients details
# # address
# # Agency_name
