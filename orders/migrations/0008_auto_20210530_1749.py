# Generated by Django 2.2.10 on 2021-05-30 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20210530_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='image',
            field=models.ImageField(blank=True, default='/static/images/pizza.jpg', upload_to='static/images'),
        ),
    ]