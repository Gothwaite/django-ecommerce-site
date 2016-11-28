from __future__ import unicode_literals
from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=30)
    price = models.CharField(max_length=10)
    quantity = models.CharField(max_length=5)
    image = models.CharField(max_length=205)
    def __unicode__(self):
        return self.name

class Orders(models.Model):
    full_name = models.CharField(max_length=30)
    product_name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    city = models.CharField(max_length=30, default = 'city')
    state = models.CharField(max_length=18)
    zipcode = models.CharField(max_length=6)
    quantity = models.CharField(max_length=5)
    total = models.CharField(max_length=10)
    ccnumber = models.CharField(max_length=16)
    ccexpiration = models.CharField(max_length=6)
    def __unicode__(self):
        return self.name

