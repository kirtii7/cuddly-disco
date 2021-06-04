from django.db import models

# Create your models here.
class Todolist(models.Model):
	Sno= models.IntegerField()
	Info= models.CharField(max_length=100)
	status= models.BooleanField()