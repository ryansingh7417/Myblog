# Generated by Django 2.2.2 on 2019-06-19 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0003_auto_20190619_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='last_scrape',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]