from django.shortcuts import get_object_or_404, redirect, render
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import *
from django.utils import timezone
from .models import *
from .forms import CheckoutForm

# Create your views here.

class HomeView(ListView):
    model = Item
    template_name = "pages/home-page.html"
    context_object_name = "items"

class ItemDetailView(DetailView):
    model = Item
    template_name = "pages/product.html"
    context_object_name = "items"


class OrderSummaryView(LoginRequiredMixin, View):
    def get(self,*args,**kwargs):
        try:
            order = Order.objects.get(user=self.request.user,ordered=False)
            context = {
                "object": order
            }
            return render(self.request, "pages/order-summary.html",context)
        except ObjectDoesNotExist:
            messages.error(self.request, "You Don't have Active Order")
            return redirect("/")
    

class CheckoutView(View):
    
    def get(self,*args, **kwargs):
        form = CheckoutForm(self.request.POST or None)
        context = {
            "form": form
        }
        return render(self.request, "pages/checkout-page.html", context)
        
    def post(self,*args, **kwargs):
        form = CheckoutForm(self.request.POST or None)
        context = {
            "form": form
        }
        if form.is_valid():
            messages.info(self.request, "form is Valid")
            return redirect("checkout")
        messages.warning(self.request,"Falied to procces form")
        return redirect("checkout")
        


@login_required
def checkout(request):
    item = Item.objects.all()
    context={
        "items": item
    }
    return render(request,"pages/checkout-page.html",context)


def profile(request):
    return redirect("/")


@login_required
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
            messages.info(request, "This item quantity was updated.")
            return redirect("product", slug=slug)
        else:
            messages.info(request, "This item was added to your cart.")
            order.items.add(order_item)
            return redirect("product", slug=slug)
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(
            user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "This item was added to your cart.")
        return redirect("product", slug=slug)


@login_required
def remove_from_cart(request,slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user, 
        ordered=False
        )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            order.items.remove(order_item)
            messages.info(request, "This item was removed from your cart.")
            return redirect("order-summary")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("product", slug=slug)
    else:
        messages.info(request, "You do not have an active order")
        return redirect("product", slug=slug)

@login_required
def remove_single_from_cart(request,slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user, 
        ordered=False
        )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order.items.remove(order_item)
            messages.info(request, "This item quantity updated")
            return redirect("order-summary")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("product", slug=slug)
    else:
        messages.info(request, "You do not have an active order")
        return redirect("product", slug=slug)

@login_required
def adding_single_from_cart(request,slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user, 
        ordered=False
        )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This item quantity updated")
            return redirect("order-summary")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("product", slug=slug)
    else:
        messages.info(request, "You do not have an active order")
        return redirect("product", slug=slug)


    

