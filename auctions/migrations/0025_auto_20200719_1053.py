# Generated by Django 3.0.8 on 2020-07-19 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0024_auto_20200719_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='bidder',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='bid',
            name='current_bid',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='bid',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='bid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bid', to='auctions.Bid'),
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=40)),
                ('listing', models.ManyToManyField(blank=True, related_name='comments', to='auctions.Listing')),
            ],
        ),
    ]