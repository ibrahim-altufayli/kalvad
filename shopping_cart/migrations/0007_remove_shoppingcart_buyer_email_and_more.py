# Generated by Django 4.1 on 2022-08-16 04:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("shopping_cart", "0006_shoppingcartproductunititem_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="shoppingcart", name="buyer_email",),
        migrations.RemoveField(model_name="shoppingcart", name="buyer_name",),
    ]
