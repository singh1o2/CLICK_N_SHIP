# Generated by Django 3.1.2 on 2020-11-10 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ShoppingApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='productImg',
        ),
    ]