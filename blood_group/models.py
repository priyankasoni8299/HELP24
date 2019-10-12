from django.db import models

# Create your models here.
class Blood(models.Model):
	Name = models.CharField(max_length=20)
	Bloodgroup_choice=(
		('A+','A-Positive'),
		('B+','B-Positive'),
		('AB+','AB-Positive'),
		('A-','A-Negative'),
		('B-','B-Negative'),
		('O+','O-Positive'),
		('O-','O-Negative'),
		('AB-','AB-Negative'),
		)
	bloodgrouptype = models.CharField(max_length=15, choices=Bloodgroup_choice)
	Age = models.IntegerField()
	Contact = models.IntegerField()
	Email = models.EmailField(max_length=50)
	city = models.CharField(max_length=20)
	def __str__(self):
		return str(self.Name)