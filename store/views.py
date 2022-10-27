from itertools import product
from django.shortcuts import render, redirect
from .models import Product, ProductColor, ProductSize
from category.models import Category
from django.http import HttpResponse
from django.db.models import Q
# Create your views here.



def store(request):
    product = Product.objects.all()

    context = {
        'product': product,
    }

    return render(request, 'store.html', context)


def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        pro_size = ProductSize.objects.all()
        pro_color = ProductColor.objects.all()

    except Exception as e:
        raise e
    context = {
        'single_product': single_product,
        'sizes': pro_size,
        'colors': pro_color,
    }

    return render(request, 'product_detail.html', context)


def category_detail(request, category_slug):
    try:
        single_category = Product.objects.filter(category__slug=category_slug)
    except Exception as e:
        raise e
    context = {
        'single_category': single_category,
    }

    return render(request, 'store.html', context)


def search(request):
    product = None
    result_count = None
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            product = Product.objects.filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword))
            result_count = product.count()
    context = {
        'product':product,
        'result_count': result_count,
    }
    return render(request, 'store.html', context)
        

