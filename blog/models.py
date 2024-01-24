from django.db import models
import datetime

class Post(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=200)
    image = models.ImageField(upload_to='blog/images')
    date = models.DateField(datetime.date.today)
    
    
