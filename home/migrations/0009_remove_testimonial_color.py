# Generated by Django 3.0.8 on 2020-08-07 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20200806_0830'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testimonial',
            name='color',
        ),
    ]