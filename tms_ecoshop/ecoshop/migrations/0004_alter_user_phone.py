# Generated by Django 4.2.6 on 2023-10-30 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecoshop', '0003_rename_product_customer_products_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=16),
        ),
    ]
