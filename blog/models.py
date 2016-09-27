from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title

class Dades(models.Model):
	id = models.AutoField(primary_key=True)
	nom = models.CharField(max_length=50)
	cognoms = models.CharField(max_length=150)
	dni = models.CharField(max_length=9) 
	data_naixament = models.DateTimeField(null=True)
	adreca = models.CharField(max_length=350)
	telefon = models.CharField(max_length=9)
	mail = models.CharField(max_length=200)
	poblacio = models.CharField(max_length=100)
	#foto		
	observacions = models.TextField()

	def __str__(self):
		return self.cognoms