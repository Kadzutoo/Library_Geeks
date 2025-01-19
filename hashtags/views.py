from django.views.generic import ListView
from .models import Product

class AllProductsView(ListView):
    model = Product
    template_name = 'products.html'
    context_object_name = 'products'

class MaleProductsView(ListView):
    model = Product
    template_name = 'products.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(tag__name='Male')

class FemaleProductsView(ListView):
    model = Product
    template_name = 'products.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(tag__name='Female')
