from itertools import product
from django.shortcuts import render, redirect
from .models import Product, ProductColor, ProductSize
from category.models import Category
from django.http import HttpResponse
from django.db.models import Q
from django.core.paginator import Paginator
from django.shortcuts import render
# Create your views here.



def store(request):
    product = Product.objects.all()
    paginator = Paginator(product, 4)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)

    context = {
        'product': paged_products,
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
        si_count = single_category.count()
        paginator = Paginator(single_category, 4)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)

    except Exception as e:
        raise e
    context = {
        'single_category': paged_products,
        'si_count': si_count,
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
        'search_products':product,
        'result_count': result_count,
    }
    return render(request, 'store.html', context)
        

