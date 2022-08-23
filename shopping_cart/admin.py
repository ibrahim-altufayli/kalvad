from django.contrib import admin
from .models import ShoppingCart, ShoppingCartProductUnitItem

# Register your models here.

admin.site.register(ShoppingCart)
admin.site.register(ShoppingCartProductUnitItem)
