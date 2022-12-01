from django.db import models

# Create your models here.
class Destination(models.Model):
    
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pic') 
    des = models.TextField()
    price = models.IntegerField()
    special = models.BooleanField(default= False)
