# Generated by Django 3.0.8 on 2020-08-07 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20200807_0533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sticky',
            name='color',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
