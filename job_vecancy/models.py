from django.db import models


# Create your models here.
class Fields(models.Model):
	field_name = models.CharField(max_length=20)
	def __str__(self):
		return self.field_name


class Vacancyinfo(models.Model):
	Company_name = models.CharField(max_length=50)
	fields = models.ForeignKey(Fields, on_delete=models.CASCADE)
	Designation = models.CharField(max_length=50)
	Experience = models.CharField(max_length=50)
	Contect = models.IntegerField()
	Email = models.EmailField()
	Address = models.CharField(max_length=50)
	city = models.CharField(max_length=50)

	def __str__(self):
		return self.Company_name



		
		