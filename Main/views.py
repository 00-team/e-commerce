from django.shortcuts import render
from .models import *

# Create your views here.

def item_list(request):
    context = {
        "items" : Item.objects.all()
    }
    return render(request,"pages/home-page.html",context)


def checkout(request):
    return render(request, "pages/checkout-page.html")


def product(request):
    return render(request, "pages/product-page.html")
