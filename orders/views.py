import time
from django.urls import reverse
from django.shortcuts import render, HttpResponseRedirect

from cart.models import Cart
from .models import Order


def orders(request):
    context = {}
    template = 'orders/user.html'
    return render(request, template, context)


def checkout(request):
    try:
        cartid = request.session['cart_id']
        cart = Cart.objects.get(id=cartid)
    except:
        cartid = None
        return HttpResponseRedirect(reverse('cart'))
    
    new_order, created = Order.objects.get_or_create(cart=cart)
    if created:
        new_order.order_id = str(time.time())
        new_order.save()

    if new_order.status == 'Finished':
        del request.session['cart_id']
        del request.session['items_total']
        return HttpResponseRedirect(reverse("cart"))


    context = {}
    template = 'orders/user.html'
    return render(request, template, context)