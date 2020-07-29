from django.db import models
from shop.models import Product

    
class Cart(models.Model):
    total = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)


    def __unicode__(self):
        return "Cart id: %s" %(self.id)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, null=True, blank=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    line_total = models.DecimalField(default=10.99, max_digits=100, decimal_places=2)
    
    def __unicode__(self):
        return self.product.name

