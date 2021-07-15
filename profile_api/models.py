from django.db import models

# Create your models here.
class Employee(models.Model):
	age = models.CharField(max_length=100)