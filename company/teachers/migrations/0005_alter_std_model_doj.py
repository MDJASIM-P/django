# Generated by Django 4.1.7 on 2023-05-09 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0004_std_model_delete_tch_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='std_model',
            name='DOJ',
            field=models.DateField(help_text='yyyy-mm-dd', verbose_name='date of joining'),
        ),
    ]