from django.db import models
from ecommerceapp.models import Product
# Create your models here.
class Cart(models.Model):
    Cart_id=models.CharField(max_length=250,blank=True)
    Date_added=models.DateField(auto_now_add=True)
    class Meta:
        db_table='Cart'
        ordering=['Date_added']
    def __str__(self):
        return '{}'.format(self.Cart_id)

class CartItem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    active=models.BooleanField(default=True)
    class Meta:
        db_table='CartItem'
    def Subtotal(self):
        return self.product.price * self.quantity
    def __str__(self):
        return '{}'.format(self.product)