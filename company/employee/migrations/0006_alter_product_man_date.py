# Generated by Django 4.1.7 on 2023-05-12 15:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0005_alter_product_man_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='man_date',
            field=models.DateField(auto_now_add=True, verbose_name=datetime.date(2023, 5, 12)),
        ),
    ]
