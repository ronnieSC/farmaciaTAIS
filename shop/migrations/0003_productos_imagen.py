# Generated by Django 3.0.8 on 2020-07-24 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20200724_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='imagen',
            field=models.ImageField(null=True, upload_to='static/images/'),
        ),
    ]