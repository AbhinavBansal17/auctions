from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="watchlist")
    listing_name = models.CharField(max_length=40)


class Bid(models.Model):
    current_bid = models.CharField(default="0.0", max_length=90)
    bidder = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.current_bid}"


class Listing(models.Model):
    bid = models.ForeignKey(Bid, on_delete=models.CASCADE, related_name="bid", default="0")
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=500)
    starting_bid = models.IntegerField()
    image = models.CharField(default="", max_length=10000)
    category = models.CharField(default="", max_length=30)
    author = models.CharField(default="", max_length=30)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title}"


class Comments(models.Model):
    author = models.CharField(max_length=40)
    comment = models.CharField(default="", max_length=10000)
    listing = models.ManyToManyField(Listing, blank=True, related_name="comments")

    def __str__(self):
        return f"{self.author}"