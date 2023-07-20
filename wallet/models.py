from django.db import models

# Create your models here.

from django.conf import settings

class Wallet(models.Model): 
        user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='wallet_users', on_delete=models.CASCADE)
        balance = models.IntegerField(default=0)