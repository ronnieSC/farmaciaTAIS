# Generated by Django 3.0.8 on 2020-08-10 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proveedor', '0003_auto_20200810_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='fechacontratacion',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='telefono',
            field=models.IntegerField(),
        ),
    ]
