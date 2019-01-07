from django.db import models
from autoslug import AutoSlugField
#from autoslug.settings import slugify 
from django.utils.text import slugify


# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name
ordering = ['name']
	
class Album(models.Model):
	author = models.ForeignKey(Artist, on_delete=models.CASCADE)
	title = models.CharField(max_length=60,default='DEFAULT_TITLE')
	songamount = models.IntegerField()
	rating = models.IntegerField()
	cover = models.FileField(null = True, blank = True)
	pubdate = models.DateTimeField('date published')
	slug = models.SlugField()
	
	def __str__(self):
		return self.title

	
	
	
	