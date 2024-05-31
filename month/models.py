from django.db import models

# Create your models here.


class Month(models.Model):
    name = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
