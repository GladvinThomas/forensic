from django.db import models

# Create your models here.



class File(models.Model):
    name=models.CharField(max_length=200)
    date=models.DateField(auto_now=True)
    case_no=models.CharField(max_length=200)

class Checks(models.Model):
    name=models.CharField(max_length=200)
    date=models.DateField(auto_now=True)
    hash1=models.CharField(max_length=200)
    hash2=models.CharField(max_length=200)
    distance=models.CharField(max_length=200)
    
    



