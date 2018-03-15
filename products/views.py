from django.shortcuts import render

# Create your views here.
from products.filters import ProductFilter
from products.models import Product, Stock


def product_view(request):
    filter = ProductFilter(request.GET, queryset=Stock.objects.all())
    context = {'filter': filter}
    return render(request, 'products/product.html', context)
