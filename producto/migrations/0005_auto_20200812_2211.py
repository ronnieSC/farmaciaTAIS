# Generated by Django 3.0.8 on 2020-08-13 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0004_auto_20200810_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.CharField(max_length=200),
        ),
    ]
