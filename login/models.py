from django.db import models

# Create your models here.
class Login(models.Model):
	firstname = models.CharField(max_length=20)
	lastname = models.CharField(max_length=20)
	email = models.CharField(max_length=30)
	password = models.CharField(max_length=20)
	def __str__(self):
		return str(self.firstname + " " + self.lastname)
