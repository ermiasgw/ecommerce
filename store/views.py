

from django.shortcuts import get_object_or_404, render

from .models import Catagory, Product


def product_all(request):
    products = Product.objects.prefetch_related("product_image").filter(is_active=True)
    return render(request, 'store/index.html', {'products': products}) 

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    return render(request, 'store/single.html', {'product': product})

def catagory_list(request, catagory_slug):
    catagory = get_object_or_404(Catagory, slug=catagory_slug)
    products = Product.objects.filter(catagory__in=Catagory.objects.get(name=catagory_slug).get_decendants(include_self=True))
    return render(request, 'store/catagory.html', {'catagory': catagory, 'products': products})