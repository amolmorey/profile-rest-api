from django.db import models

# Create your models here.
class Employee(models.Model):
	user1 = models.CharField(max_length=100)
	name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	fiest = models.CharField(max_length=200)
	age = models.IntegerField(max_length=200)
	amount = models.IntegerField(max_length=200)