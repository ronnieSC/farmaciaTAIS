# Generated by Django 3.0.8 on 2020-08-10 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proveedor', '0004_auto_20200810_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='fechacontratacion',
            field=models.TextField(),
        ),
    ]
