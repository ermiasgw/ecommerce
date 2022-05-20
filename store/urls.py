from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
   path('', views.all_products, name='all_products'),
   path('item/<slug:slug>/', views.product_detail, name='product_detail'),
   path('search/<slug:catagory_slug>/', views.catagory_list, name='catagory_list'),
]