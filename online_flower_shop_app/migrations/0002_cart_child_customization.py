# Generated by Django 4.2.5 on 2024-02-19 05:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('online_flower_shop_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart_child_customization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Assign_Date', models.CharField(max_length=100)),
                ('Del_Date', models.CharField(max_length=100)),
                ('Delivery_Status', models.CharField(max_length=100)),
                ('CART_CHILD', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='online_flower_shop_app.tbl_cartchild')),
                ('ITEM', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='online_flower_shop_app.tbl_itemchild')),
            ],
        ),
    ]