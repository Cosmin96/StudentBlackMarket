from django.contrib import admin

# Register your models here.
from .models import Product, Request

admin.site.register(Product)
admin.site.register(Request)