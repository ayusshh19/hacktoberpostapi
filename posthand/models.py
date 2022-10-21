from django.db import models

# Create your models here.
class Postapi(models.Model):
    designation=models.CharField(max_length=100)
    company=models.CharField(max_length=100)
    description=models.CharField(max_length=1000)
    location=models.CharField(max_length=200)