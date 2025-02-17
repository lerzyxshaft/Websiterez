from zoneinfo import available_timezones

from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.core.paginator import Paginator

def popular_list(request):
    products = Product.objects.filter(available = True)[:3]
    return render(request,
                  'main/index/index.html',
                  {'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product,
                                 slug=slug,
                                 available=True)

    return render(request,
                  'main/product/detail.html',
                  {'product': product})

def product_list(request, category_slug=None):
    page = request.Get('page', 1)
    category = None
    categories = Category.objects.all
    paginator = Paginator(products, 1)
    current_page = paginator.page(int(page))
    products = Product.objects.filter(available = True)
    if category_slug:
        category = get_object_or_404(Category,
                                     slug=category_slug)
        paginator = Paginator(products.filter(category=category), 1)
        current_page = paginator.page(int(page))
    return render(request,
                  'main/product/list.html',
                    {"category": category,
                    'categories': categories,
                    'products': current_page,
                     'slug_url': category_slug})
