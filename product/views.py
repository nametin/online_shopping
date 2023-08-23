from django.shortcuts import render
from .models import Product

# Create your views here.


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
    
def list(request):
    recent_products = Product.objects.filter().order_by('-time')[:12]
    
    if request.GET['q'] and request.GET['q'] is not None:
        q = request.GET['q']    
        products = Product.objects.filter(product_name__contains=q)
    else: 
        products = list()
        
    return render(request, "common/category.html", {
        "products": products,
        "recent_products": recent_products,
        "search": True,
        "query": q,
        }
    )
    