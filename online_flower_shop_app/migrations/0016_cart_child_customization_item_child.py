# Generated by Django 4.2.5 on 2024-03-01 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('online_flower_shop_app', '0015_remove_cart_child_customization_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart_child_customization',
            name='ITEM_CHILD',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='online_flower_shop_app.tbl_itemchild'),
        ),
    ]