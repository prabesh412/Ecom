from django.contrib import admin
from .models import product, Category, cart
# Register your models here.

admin.site.register(product)
admin.site.register(Category)
admin.site.register(cart)
