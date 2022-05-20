from nis import cat
from django.shortcuts import get_object_or_404, render

from .models import Catagory, Product

def catagories(request):
    return {
        'catagories': Catagory.objects.all()
    }

def all_products(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products}) 

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/products/detail.html', {'product': product})

def catagory_list(request, catagory_slug):
    catagory = get_object_or_404(Catagory, slug=catagory_slug)
    products = Product.objects.filter(catagory=catagory)
    return render(request, 'store/products/catagory.html', {'catagory': catagory, 'products': products})