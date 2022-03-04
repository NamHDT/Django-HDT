# Generated by Django 4.0.2 on 2022-02-26 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_alter_line_item_order_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='line_item_order',
            name='fulfillment_status',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='line_item_order',
            name='price',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='order',
            name='city',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]