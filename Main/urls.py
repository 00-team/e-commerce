from django.urls import path,include
from .views import *

urlpatterns = [
    path("",item_list,name="item-list"),
    path("checkout/", checkout, name="checkout"),
    path("product/", product, name="product"),
]
