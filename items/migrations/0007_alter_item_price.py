# Generated by Django 5.1.6 on 2025-02-28 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0006_order_alter_item_currency_orderitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена'),
        ),
    ]
