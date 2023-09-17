from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Listing, Bid, Comments, Watchlist


def index(request):
    return render(request, "auctions/index.html", {
        "listings": Listing.objects.all().filter(is_active=True), "title":
        "Active Listings"
    })


listing_closed = False


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


@login_required(login_url='/login')
def create_listing(request):
    if request.user.is_authenticated:
        current_user = request.user.username
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        starting_bid = request.POST["starting_bid"]
        image = request.POST["image"]
        category = request.POST["category"]

        try:
            bid = Bid(current_bid="0", bidder=current_user)
            bid.save()
            listing = Listing(title=title, description=description, starting_bid=starting_bid, image=image, category=category, author=current_user, bid=bid, is_active=True)
            listing.save()
        except IntegrityError:
            print(IntegrityError)
            return render(request, "auctions/create_listing.html", {
                "message": "Listing already exists"
            })

        return HttpResponseRedirect(reverse("index"), {
            "message": "Listing Created"
        })
    return render(request, "auctions/create_listing.html")


@login_required(login_url='/login')
def listing(request, title):
    listing = Listing.objects.get(title=title)
    return render(request, "auctions/listing.html", {
        "listing": listing, "comments": Comments.objects.filter(listing=listing), "bid": int(listing.bid.current_bid)
    })


@login_required(login_url='/login')
def categories(request):
    return render(request, "auctions/categories.html")


@login_required(login_url='/login')
def category(request, name):
    listings = Listing.objects.all().filter(category=name)
    return render(request, "auctions/category.html", {
        "listings": listings, "category": name
    })

@login_required
def bid(request, listing):
    if request.user.is_authenticated:
        current_user = request.user.username
    if request.method == "POST":
        current_bid = request.POST["bid"]
        check = Listing.objects.get(title=listing)
        if check.starting_bid < int(current_bid):
            if int(check.bid.current_bid) < int(current_bid):
                bid = Bid(current_bid=current_bid, bidder=current_user)
                bid.save()
                a = Listing.objects.get(title=listing)
                a.bid = bid
                a.save()
                return render(request, "auctions/listing.html", {
                    "listing": Listing.objects.get(title=listing)
                })
            else:
                return render(request, "auctions/listing.html", {
                    "listing": Listing.objects.get(title=listing), "message": "The entered bid must be higher than the current bid."
                })
        else:
            return render(request, "auctions/listing.html", {
                "listing": Listing.objects.get(title=listing), "message": "The entered bid must be higher than the starting bid."
            })
    return render(request, "auctions/index.html")


@login_required
def close_auction(request, title):
    listing = Listing.objects.get(title=title)
    listing.is_active = False
    listing.save()
    return render(request, "auctions/listing.html", {
        "listing": Listing.objects.get(title=title)
    })


@login_required
def closed_listings(request):
    return render(request, "auctions/index.html", {
        "listings": Listing.objects.all().filter(is_active=False), "title": "Closed Listings: Check to see if you are a winner.",

    })


@login_required
def comment(request, title):
    if request.user.is_authenticated:
        current_user = request.user.username
    if request.method == "POST":
        comments = request.POST["comment"]
        listings = Listing.objects.get(title=title)
        comment = Comments(comment=comments, author=current_user)
        comment.save()
        comment.listing.add(listings)
        return render(request, "auctions/listing.html", {
            "listing": listings, "comments": Comments.objects.filter(listing=listings),
            "bid": int(listings.bid.current_bid)
        })

    return render(request, "auctions/index.html")


@login_required
def watchlist(request):
    if request.user.is_authenticated:
        current_user = request.user.username
        user_id = request.user.id
    items = Watchlist.objects.filter(user=user_id).count()
    return render(request, "auctions/watchlist.html", {
        "listings": Watchlist.objects.filter(user=user_id), "current_user": current_user, "items": items})


@login_required
def add_to_watchlist(request, title):
    user = User.objects.all().get(username=request.user.username)
    listing = Watchlist(user=user, listing_name=title)
    listing.save()
    return HttpResponseRedirect(reverse("watchlist"))


@login_required
def remove_from_watchlist(request, title):
    listing = Watchlist.objects.filter(user=User.objects.all().get(username=request.user.username), listing_name=title)
    listing.delete()
    return HttpResponseRedirect(reverse("watchlist"))