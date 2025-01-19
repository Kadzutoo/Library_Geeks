from django.views.generic import TemplateView, ListView, View
from django.shortcuts import redirect, get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Product, Cart, CartItem

@method_decorator(login_required, name='dispatch')
class CartView(ListView):
    model = CartItem
    template_name = 'cart/cart_view.html'
    context_object_name = 'cart_items'

    def get_queryset(self):
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        return cart.items.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = Cart.objects.get(user=self.request.user)
        context['total_price'] = cart.total_price()
        return context

@method_decorator(login_required, name='dispatch')
class AddToCartView(View):
    def post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            cart_item.quantity += 1
            cart_item.save()
        return redirect('cart_view')

@method_decorator(login_required, name='dispatch')
class RemoveFromCartView(View):
    def post(self, request, product_id):
        cart = Cart.objects.get(user=request.user)
        cart_item = get_object_or_404(CartItem, cart=cart, product_id=product_id)
        cart_item.delete()
        return redirect('cart_view')
