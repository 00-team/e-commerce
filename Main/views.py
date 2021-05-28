from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import *
from django.utils import timezone
from .models import *

# Create your views here.

class HomeView(ListView):
    model = Item
    template_name = "pages/home-page.html"
    context_object_name = "items"

class ItemDetailView(DetailView):
    model = Item
    template_name = "pages/product.html"
    context_object_name = "items"

def checkout(request):
    return render("pages/checkout-page.html")

# def add_to_cart(request,slug):
#     item = get_object_or_404(Item,slug=slug)
#     order_item = OrderItem.objects.create(item=item)
#     order_qs = Order.objects.filter(user=request.user,ordered=False)
#     if order_qs.exists():
#         order = order_qs[0]
#         if order.items.filter(item__slug=item.slug).exists():
#             order_item.quautity += 1
#             order_item.save()
#     else:
#         ordered_date = timezone.now()
#         order = Order.objects.create(
#             user=request.user, ordered_date=ordered_date)
#         order.items.add(order_item)
#     return redirect("product", slug=slug)


def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
        )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
        else:
            order.items.add(order_item)
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(
            user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)

    return redirect("product", slug=slug)

    

