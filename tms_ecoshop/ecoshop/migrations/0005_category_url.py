# Generated by Django 4.2.6 on 2023-10-30 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecoshop', '0004_alter_user_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='url',
            field=models.CharField(default='Wrong', max_length=100),
        ),
    ]
