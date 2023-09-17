from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create_listing", views.create_listing, name="create_listing"),
    path("listing/<str:title>", views.listing, name="listing"),
    path("category/<str:name>", views.category, name="category"),
    path("categories>", views.categories, name="categories"),
    path("bid/<str:listing>", views.bid, name="bid"),
    path("close/<str:title>", views.close_auction, name="close_auction"),
    path("closed_listings", views.closed_listings, name="closed_listings"),
    path("comment/<str:title>", views.comment, name="comment"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("add_to_watchlist/<str:title>", views.add_to_watchlist, name="add_to_watchlist"),
    path("remove_from_watchlist/<str:title>", views.remove_from_watchlist, name="remove_from_watchlist"),

]
