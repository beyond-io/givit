from django.db import models

# Create your models here.
REGION_CHOICES = [
    ('Tel Aviv','Tel Aviv'),
    ('Jerusalem','Jerusalem'),
    ('Beer Sheva','Beer Sheva'),
    ('Haifa','Haifa'),
    ('Modiin','Modiin'),
    ('Hasharon','Hasharon'),
]

ITEM_CHOICES = [
    ('table','table'),
    ('bed','bed'),
    ('TV','TV'),
    ('washing machine','washing machine'),
    ('fridge','fridge'),
    ('oven','oven'),
    ('microwave oven','microwave oven'),
    ('chair','chair'),
    ('computer screen','computer screen'),
    ('keyboard','keyboard'),
    ('laptop','laptop'),
    ('closet','closet'), 
]
STATUS_CHOICES = [
    ('open','open'),
    ('closed','closed'),
]

class ItemRequest(models.Model):
    #friennd ID inherite from user table
    friend_id = models.IntegerField(default = 305355356)
    item = models.CharField(max_length = 40,choices = ITEM_CHOICES)
    region = models.CharField(max_length = 40,choices = REGION_CHOICES)
    special_req= models.TextField(blank=True)
    status = models.CharField(max_length = 40,default = 'open', choices = STATUS_CHOICES)
    