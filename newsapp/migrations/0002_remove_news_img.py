# Generated by Django 2.2.2 on 2019-06-19 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='img',
        ),
    ]
