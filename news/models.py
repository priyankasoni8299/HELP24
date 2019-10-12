from django.db import models
class News(models.Model):
	news_type = models.CharField(max_length=50)
	def __str__(self):
		return self.news_type

class Newsinfo(models.Model):
	News_entry = models.CharField(max_length=50)
	news = models.ForeignKey(News, on_delete=models.CASCADE)
	data = models.CharField(max_length=2000)
	image = models.ImageField()
	#Time = models.TimeField()
	date = models.DateTimeField()
	city = models.CharField(max_length=50)
	state = models.CharField(max_length=50)
	def __str__(self):
		return self.News_entry
	# Create your models here.


