# Generated by Django 3.0.8 on 2020-07-22 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0031_comments_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='in_watchlist',
            field=models.BooleanField(default=False),
        ),
    ]