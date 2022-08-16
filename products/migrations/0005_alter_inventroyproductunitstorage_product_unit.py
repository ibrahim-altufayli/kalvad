# Generated by Django 4.1 on 2022-08-15 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0004_remove_inventroyproductunitstorage_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="inventroyproductunitstorage",
            name="product_unit",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                primary_key=True,
                related_name="inventroy_product_unit_storage",
                serialize=False,
                to="products.productunit",
            ),
        ),
    ]
