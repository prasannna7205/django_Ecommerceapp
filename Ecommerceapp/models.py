from django.db import models

# Create your models here.
class Useradd(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    price=models.IntegerField()
    quantity=models.CharField(max_length=100)