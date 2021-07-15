from django.db import models

# Create your models here.
class Employee(models.Model):
	username = models.CharField(max_length=100)