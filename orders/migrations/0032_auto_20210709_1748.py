# Generated by Django 2.2.10 on 2021-07-09 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0031_remove_completed_order_ids_order_detail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='completed_order_ids',
            old_name='user',
            new_name='user_id',
        ),
        migrations.AddField(
            model_name='completed_order_ids',
            name='order_detail',
            field=models.CharField(default=1, max_length=800),
            preserve_default=False,
        ),
    ]