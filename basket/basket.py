

from store.models import Product
from decimal import Decimal
from django.conf import settings



class Basket():
    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('skey')
        if 'skey' not in request.session:
            basket = self.session['skey'] = {}
        self.basket = basket

    def add(self, product, product_qty):
        """
        Adding and updating the users basket
        """

        product_id = str(product.id) 

        if product_id not in self.basket:
            self.basket[product_id] = {'price': str(product.regular_price), 'qty': int(product_qty)}
        else:
            self.basket[product_id]['qty'] = self.basket[product_id]['qty'] + int(product_qty)

        self.session.modified = True 
    
    def __len__(self):
        return sum(item['qty'] for item in self.basket.values())

    def __iter__(self):
        product_ids = self.basket.keys()
        products = Product.objects.filter(id__in=product_ids)
        basket = self.basket.copy()
        for product in products:
            basket[str(product.id)]['product'] = product
        
        for item in basket.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['qty']
            yield item
    def get_total_price(self):
        return sum(Decimal(item['price']) * item['qty'] for item in self.basket.values())

    def delete(self, product):
        product_id = str(product)

        if product_id in self.basket:
            del self.basket[product_id]
            self.save()
    
    def save(self):
        self.session.modified = True

    def update(self, product, qty):
        product_id = str(product)
        qty = qty
        if product_id in self.basket:
            self.basket[product_id]['qty'] = qty
            self.save()

    def clear(self):
        del self.session['skey']
        self.save()