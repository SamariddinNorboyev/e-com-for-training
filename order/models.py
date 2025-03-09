from django.db import models
from products.models import Product
# Create your models here.
class Order(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')
    count = models.IntegerField(default=0)