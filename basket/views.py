
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from store.models import Product
from . basket import Basket
from django.http import JsonResponse

# Create your views here.
def basket_summary(request):
    basket = Basket(request)
    return render(request, 'store/basket/summary.html', {'basket': basket})

def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        product = get_object_or_404(Product, id=product_id)
        basket.add(product, product_qty)

        b = basket.__len__()
        response = JsonResponse({'qty': b})
        return response

