# Generated by Django 4.0.2 on 2022-02-25 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_alter_line_item_order_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='line_item_order',
            name='order',
            field=models.CharField(max_length=50, null=True),
        ),
    ]