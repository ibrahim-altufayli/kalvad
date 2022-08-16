from email.policy import default
from random import choices
from django.db import models
from django.utils.translation import gettext_lazy as _
from products.models import ProductUnit

class CartStatus(models.TextChoices):
        OPPENED = "OE", _("Oppened")
        CONFIRMED = "CF", _("Confirmed")
        DISCARDED = "DC", _("Discarded")

# Create your models here.
class ShoppingCart(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    close_date = models.DateTimeField(null=True, blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    shopping_cart_product_units = models.ManyToManyField(ProductUnit, related_name= "shoping_carts",through='ShoppingCartProductUnitItem')
    status = models.CharField(max_length= 2, choices=CartStatus.choices, default=CartStatus.OPPENED)

    def __str__(self) -> str:
        return self.id

class ShoppingCartProductUnitItem(models.Model):
    shopping_cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE, related_name="shopping_cart_product_unit_items")
    product_unit = models.ForeignKey(ProductUnit, on_delete=models.DO_NOTHING)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    quantity = models.IntegerField(null=False)

    def __str__(self) -> str:
         return str(self.shopping_cart.id) + " | " + self.product_unit.product.name + " | " + self.product_unit.name + " | " + str(self.quantity)


