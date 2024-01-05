# Generated by Django 3.0.8 on 2020-08-06 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('proveedor', models.CharField(max_length=100)),
                ('precio', models.FloatField()),
                ('cantidad', models.IntegerField()),
                ('oferta', models.BooleanField()),
                ('imagen', models.ImageField(null=True, upload_to='static/images/')),
            ],
        ),
    ]
