from django.shortcuts import render, get_object_or_404
from .models import Product


def home(request):
    products = Product.objects
    return render(request, 'shop/home.html', {'products':products})

def detail(request, blog_id):
    detailproduct = get_object_or_404(Product, pk=blog_id)
    return render(request, 'shop/detail.html', {'detailproduct': detailproduct})