from django.shortcuts import render, get_object_or_404
from .models import Product


def home(request):
    products = Product.objects
    template = 'shop/home.html'
    context = {'products':products}
    return render(request, template, context)

def detail(request, slug):
    detailproduct = get_object_or_404(Product, slug=slug)
    template = 'shop/detail.html'
    context = {'detailproduct': detailproduct}
    return render(request, template, context)