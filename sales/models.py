
from django.db import models

class Product(models.Model):
    upc_code = models.CharField(max_length=12, unique=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.upc_code}: {self.name} - ${self.price}'

