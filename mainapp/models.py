from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):
	name = models.CharField(max_length = 200)
	category = models.CharField(max_length = 200)
	price = models.CharField(max_length = 50)
	location = models.CharField(max_length = 100)
	creator = models.ForeignKey(User, on_delete=models.CASCADE)
	description =  models.CharField(max_length = 1000)
	file =models.ImageField(upload_to='files')

class Request(models.Model):
	creator = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length = 200)
	category = models.CharField(max_length = 200)
	location = models.CharField(max_length = 100)
	description =  models.CharField(max_length = 1000)