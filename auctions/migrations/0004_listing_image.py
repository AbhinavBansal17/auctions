# Generated by Django 3.0.8 on 2020-07-15 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auto_20200715_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='image',
            field=models.CharField(default='', max_length=10000),
        ),
    ]
