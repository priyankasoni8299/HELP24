from django.db import models

class Categories(models.Model):
	category_name = models.CharField(max_length=20)

	def __str__(self):
		return str(self.category_name)

class Directory_info(models.Model):
	name = models.CharField(max_length=50)
	category = models.ForeignKey(Categories, on_delete=models.CASCADE)
	email = models.EmailField()
	address = models.CharField(max_length=100)
	city = models.CharField(max_length=20)
	Contact = models.IntegerField()
	image = models.ImageField(upload_to='')
	def __str__(self):
		return str(self.name)

