from django.urls import path,include
from .views import *

urlpatterns = [
    path("",HomeView.as_view(),name="item-list"),
    path("checkout/", checkout, name="checkout"),
    path("product/<slug>/", ItemDetailView.as_view(), name="product"),
]
