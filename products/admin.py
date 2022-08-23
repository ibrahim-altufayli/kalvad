from django.contrib import admin
from .models import Product, ProductUnit, InventoryProductUnitStorage

# Register your models here.
admin.site.register(Product)
admin.site.register(ProductUnit)
admin.site.register(InventoryProductUnitStorage)
