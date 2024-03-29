# Generated by Django 4.2.6 on 2023-11-20 16:42

from django.db import migrations, models
import ecoshop.models


class Migration(migrations.Migration):

    dependencies = [
        ('ecoshop', '0007_alter_category_photo_alter_customer_photo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='photo',
            field=models.ImageField(default='image_not_found.jpg', upload_to=ecoshop.models.user_dir_photo),
        ),
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(default='image_not_found.jpg', upload_to=ecoshop.models.user_dir_photo),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='photo',
            field=models.ImageField(default='image_not_found.jpg', upload_to=ecoshop.models.user_dir_photo),
        ),
    ]
