from django.db import models

# Create your models here.
class  Merchant(models.Model):
    merchant_name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
