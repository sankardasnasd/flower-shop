# Generated by Django 4.2.5 on 2024-02-19 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('online_flower_shop_app', '0007_tbl_staff_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_delivery',
            name='STAFF',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='online_flower_shop_app.tbl_staff'),
            preserve_default=False,
        ),
    ]