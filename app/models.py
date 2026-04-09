from django.db import models

# Create your models here.

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()  # in INR

class Order(models.Model):
    stripe_session_id = models.CharField(max_length=255, unique=True, null=True, blank=True)
    is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()