from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Out door', 'Out door'),
    )

    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag, )
    image = models.ImageField(upload_to='products/', default="")
    vendor = models.CharField(max_length=200, null=True, blank=True)
    ratings = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )

    Payment_Modes = (
        ('Net Banking', 'Net Banking'),
        ('Cash on Delivery', 'Cash on Delivery'),
        ('Card Payment', 'Card Payment'),
    )

    customer = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE
    )
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField(default=1)
    mode_of_payment = models.CharField(max_length=100, null=True, choices=Payment_Modes)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=100, null=True, choices=STATUS)
    address = models.TextField(max_length=200, null=True)

    def __str__(self):
        return "{} ({})".format(self.customer, self.product)


class Cart(models.Model):
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    customer = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE
    )

    def __str__(self):
        return "{} ({})".format(self.customer, self.product)
