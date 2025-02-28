# Generated by Django 5.1.6 on 2025-02-27 15:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_item_currency_order_discount_tax'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='discount',
            name='order',
        ),
        migrations.RemoveField(
            model_name='tax',
            name='order',
        ),
        migrations.AddField(
            model_name='order',
            name='discount',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='items.discount'),
        ),
        migrations.AddField(
            model_name='order',
            name='tax',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='items.tax'),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.IntegerField(default=0),
        ),
    ]
