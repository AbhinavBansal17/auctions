# Generated by Django 3.0.8 on 2020-07-16 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_listing_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_bid', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='listing',
            name='current_bid',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='auctions.Bid'),
        ),
    ]