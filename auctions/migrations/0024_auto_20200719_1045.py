# Generated by Django 3.0.8 on 2020-07-19 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0023_auto_20200719_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='current_bid',
            field=models.CharField(max_length=30),
        ),
    ]