# Generated by Django 3.0.5 on 2020-04-24 00:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='post',
        ),
    ]
