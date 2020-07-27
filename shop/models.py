from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=100)
    description = models.CharField(max_length=400, default='')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=7.00)

    def __str__(self):
        return self.name
