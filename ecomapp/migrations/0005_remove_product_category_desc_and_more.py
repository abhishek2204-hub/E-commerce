# Generated by Django 4.2.5 on 2024-06-20 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0004_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product_category',
            name='desc',
        ),
        migrations.RemoveField(
            model_name='product_category',
            name='price',
        ),
    ]
