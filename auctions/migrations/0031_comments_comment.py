# Generated by Django 3.0.8 on 2020-07-19 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0030_auto_20200719_1359'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='comment',
            field=models.CharField(default='', max_length=10000),
        ),
    ]
