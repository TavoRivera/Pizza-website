# Generated by Django 2.2.10 on 2021-05-29 05:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_toppingcount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itemcost',
            old_name='name',
            new_name='size',
        ),
    ]