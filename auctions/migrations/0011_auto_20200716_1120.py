# Generated by Django 3.0.8 on 2020-07-16 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_listing_current_bid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]