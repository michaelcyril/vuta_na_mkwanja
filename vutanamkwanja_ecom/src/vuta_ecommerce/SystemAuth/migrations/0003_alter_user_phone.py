# Generated by Django 3.2.15 on 2022-09-20 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SystemAuth', '0002_user_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=10),
        ),
    ]