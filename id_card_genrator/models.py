from django.db import models

# Create your models here.

class studentinfo(models.Model):
    name = models.CharField(max_length=500)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()
    college = models.CharField(max_length=500)
    country = models.CharField(max_length=50)
