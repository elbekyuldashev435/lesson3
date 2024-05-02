from django.shortcuts import render
from .models import Category, Product
# Create your views here.


def get_info(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'index.html', context=context)


def get_products(request, pk):
    products = Product.objects.filter(category=pk)
    context = {
        'products': products
    }
    return render(request, 'products.html', context=context)