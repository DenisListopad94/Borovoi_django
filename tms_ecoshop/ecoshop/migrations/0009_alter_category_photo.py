# Generated by Django 4.2.6 on 2023-11-22 09:18

from django.db import migrations, models
import ecoshop.models


class Migration(migrations.Migration):

    dependencies = [
        ('ecoshop', '0008_alter_customer_photo_alter_product_photo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='photo',
            field=models.ImageField(default='image_not_found.jpg', upload_to=ecoshop.models.user_dir_photo),
        ),
    ]
