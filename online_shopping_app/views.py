from django.shortcuts import render
from django.db.models import Q

from product.models import Product

def index(request):
    products = Product.objects.all()[:12]
    recent_products = Product.objects.filter().order_by('-time')[:12]
    return render(request, "root/index.html",{
        "products": products,
        "recent_products": recent_products,
    })

def category(request,category):
    products = Product.objects.filter(Q(category__iexact=category))
    recent_products = Product.objects.filter().order_by('-time')[:12]
    return render(request, "root/category.html", {
        "category" : category,
        "products": products,
        "recent_products": recent_products,
        "search": False,
    }
)

def contact(request):
    return render(request, "root/contact.html")
