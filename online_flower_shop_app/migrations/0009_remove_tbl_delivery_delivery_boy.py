# Generated by Django 4.2.5 on 2024-02-19 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('online_flower_shop_app', '0008_tbl_delivery_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_delivery',
            name='delivery_boy',
        ),
    ]