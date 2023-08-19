from django.shortcuts import render
from .models import Product
# Create your views here.
def details(request, product_id):
    p=Product.objects.get(id=product_id)
    
    return render(request, "product/details.html", {"product": p})
