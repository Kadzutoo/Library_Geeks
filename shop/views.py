from django.shortcuts import render, redirect
from .models import Product, Cart, CartItem


def cart(request):
    if request.method == 'GET':
        cart = Cart.objects.all()
        return render(request, 'cart/cart_view.html', {'cart': cart})


def add_to_cart(request, product_id):
    if request.method == 'GET':
        add_to_cart= Product.objects.get(pk=product_id)
        return render(request, 'cart/add_to_cart.html', {'add_to_cart': add_to_cart})


def remove_from_cart(request, product_id):
    if request.method == 'GET':
        remove_from_cart = Product.objects.get(pk=product_id)
        return render(request, 'cart/cart_list.html', {'remove_from_cart': remove_from_cart})