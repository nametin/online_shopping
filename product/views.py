from django.shortcuts import render
from .models import Product
from django.db.models import Q

# Create your views here.

def index(request):
    products = Product.objects.all()[:12]
    recent_products = Product.objects.filter().order_by('-time')[:12]
    return render(request, "product/index.html",{
        "products": products,
        "recent_products": recent_products,
    })

def details(request, product_id):
    product=Product.objects.get(product_id=product_id)
    # burada bu sql sorgusunun çalışmasına aslında gerek yok. 
    image_urls = product.images.all()
    products = Product.objects.filter(category=product.category).exclude(product_id=product_id)

    return render(request, "product/details.html", 
        {
        "product": product, 
        "image_urls": image_urls,
        "products": products,
        }
    )
    
def category(request,category):
    products = Product.objects.filter(Q(category__iexact=category))
    recent_products = Product.objects.filter().order_by('-time')[:12]
    return render(request, "product/category.html", {
        "category" : category,
        "products": products,
        "recent_products": recent_products,
        "search": False,
    }
)

def list(request):
    recent_products = Product.objects.filter().order_by('-time')[:12]
    
    if request.GET['q'] and request.GET['q'] is not None:
        q = request.GET['q']    
        products = Product.objects.filter(product_name__contains=q)
    else: 
        products = list()
        
    return render(request, "product/category.html", {
        "products": products,
        "recent_products": recent_products,
        "search": True,
        "query": q,
        }
    )