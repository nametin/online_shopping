from django.shortcuts import render
from .models import Product
# Create your views here.
def details(request, product_id):
    p=Product.objects.get(product_id=product_id)
    image_urls = p.images.all()
    return render(request, "product/details.html", {"product": p, "image_urls": image_urls})
