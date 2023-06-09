from django.db import models

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    inventory = models.IntegerField()
    
    def offer_price(self):
        return self.price + self.inventory