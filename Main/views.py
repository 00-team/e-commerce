from django.shortcuts import render
from django.views.generic import *
from .models import *

# Create your views here.

class HomeView(ListView):
    model = Item
    template_name = "pages/home-page.html"
    context_object_name = "items"

class ItemDetailView(DetailView):
    model = Item
    template_name = "pages/product.html"



def checkout(request):
    return render(request, "pages/checkout-page.html")

