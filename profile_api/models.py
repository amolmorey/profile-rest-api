from django.db import models

# Create your models here.
class Employee(models.Model):
	user = models.CharField(max_length=100)
	name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	