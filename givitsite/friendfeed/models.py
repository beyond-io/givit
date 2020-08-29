from django.db import models

# Create your models here.
class FoundItem(models.Model):
    request_id = models.IntegerField()
    url = models.CharField(max_length=200)
    picture = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=12) 

    
