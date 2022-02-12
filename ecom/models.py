from math import prod
from sre_constants import CATEGORY
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=40)
        
    def __str__(self):
        return self.name


class product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    product_image= models.ImageField(upload_to='images/', null=True)
    price = models.FloatField()
    pub_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.product_name

    def title(self):
        name = str(self.product_name)
        return name.upper()

    def stringcat(self):
        return str(self.category)

class cart(models.Model):
    customer = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    products = models.ForeignKey(product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=1, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.products)

class comments(models.Model):
    item = models.ForeignKey(product, null=True, blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True,blank=True,on_delete=models.CASCADE)
    body = models.CharField(max_length=30)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)