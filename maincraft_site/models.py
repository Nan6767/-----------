from django.db import models

# Create your models here.

class user(models.Model):
    user_id = models.IntegerField
    nickname = models.CharField(100)
    password = models.CharField(16)
    email = models.CharField(255)
    phone_number = models.CharField(20)
    
class card(models.Model):
    cost = models.IntegerField
    name = models.CharField(255)ш