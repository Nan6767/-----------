from django.db import models

# Create your models here.

class user(models.Model):
    user_id = models.IntegerField
    nickname = models.CharField(max_length=100)
    password = models.CharField(max_length=16)
    email = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    
class card(models.Model):
    cost = models.IntegerField
    name = models.CharField(max_length=255)