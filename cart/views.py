from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .models import Cart, CartItem
from shop.models import Product


def view(request):
    try:
        cartid = request.session['cart_id']
        cart = Cart.objects.get(id=cartid)
    except:
        cartid = None
    if cartid:
        request.session['items_total'] = sum([item.quantity for item in cart.cartitem_set.all()])
        cart.total = sum([float(item.product.price) * item.quantity for item in cart.cartitem_set.all()])
        cart.save()
        context = {"cart": cart}
    else:
        empty_message = "Your Cart is empty"
        context = {"empty": True, "empty_message": empty_message}

    template = "cart/view.html"
    return render(request, template, context)

def remove_from_cart(request, id):
    print("I am here")
    try:
        cartid = request.session['cart_id']
        cart = Cart.objects.get(id=cartid)
    except:
        HttpResponseRedirect(reverse("cart"))
    cartitem = CartItem.objects.get(id=id)
    cartitem.cart = None
    cartitem.save()
    return HttpResponseRedirect(reverse("cart"))


def update_cart(request, slug):
    print("I shouldnt be here")
    request.session.set_expiry(3600 * 3)
    try:
        qty = request.GET.get('qty')
        update_qty = True
    except:
        qty = None
        update_qty = False
    
    try:
        cartid = request.session['cart_id']
    except:
        new_cart = Cart()
        new_cart.save()
        request.session['cart_id'] = new_cart.id
        cartid = new_cart.id
    
    cart = Cart.objects.get(id=cartid)
    try:
        product = Product.objects.get(slug=slug)
    except Product.DoesNotExist:
        pass
    except:
        pass
    
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if update_qty and qty:
        if int(qty) == 0:
            cart_item.delete()
        else:
            cart_item.quantity = qty
            cart_item.save()
    else:
        pass

    return HttpResponseRedirect(reverse("cart"))
