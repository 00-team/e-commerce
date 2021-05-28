from django.urls import path,include
from .views import *

urlpatterns = [
    path("",HomeView.as_view(),name="item-list"),
    path("checkout/", checkout, name="checkout"),
    path("product/<slug>/", ItemDetailView.as_view(), name="product"),
    path("add-to-cart/<slug>/", add_to_cart, name="add-to-cart"),
    path("remove-from-cart/<slug>/", remove_from_cart, name="remove-from-cart"),
]
