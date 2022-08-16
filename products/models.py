from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(null=False, max_length=50) 
    description = models.CharField(null=False, max_length=255)
    image = models.ImageField(upload_to="product_images")
        
    def __str__(self) -> str:
        return self.name

class ProductUnit(models.Model):
    name = models.CharField(null=False, max_length=50)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_units")
    price = models.DecimalField(null=False, max_digits=10, decimal_places=2, default=0)
    is_default = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        super(ProductUnit, self).save(*args, **kwargs)
        # one Default Product Unit should be exsit for specific Product
        if self.is_default : 
            Product.objects.get(pk=self.product.id).product_units.exclude(pk=self.id).update(is_default= False)
        # create new Inventory Storage Record for newly created Product Units
        if not hasattr(self, 'inventroy_product_unit_storage'):
            inventeryProductUnitStorage = InventroyProductUnitStorage(product_unit = self, quantity = 0)
            inventeryProductUnitStorage.save()

    def __str__(self) -> str:
        return self.product.name + " | " + self.name


class InventroyProductUnitStorage(models.Model):
    product_unit = models.OneToOneField(ProductUnit, on_delete=models.CASCADE, primary_key=True, related_name="inventroy_product_unit_storage")
    quantity = models.IntegerField(null=False, default=0)

    def __str__(self) -> str:
        return self.product_unit.product.name + " | " + self.product_unit.name




