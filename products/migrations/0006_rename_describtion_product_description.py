# Generated by Django 4.1 on 2022-08-15 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0005_alter_inventroyproductunitstorage_product_unit"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product", old_name="describtion", new_name="description",
        ),
    ]
