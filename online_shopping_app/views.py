from django.shortcuts import render
from django.db.models import Q

from product.models import Product

from utils.common import mail

def index(request):
    products = Product.objects.all()[:12]
    recent_products = Product.objects.filter().order_by('-time')[:12]
    return render(request, "common/index.html",{
        "products": products,
        "recent_products": recent_products,
    })

def category(request,category):
    products = Product.objects.filter(Q(category__iexact=category))
    recent_products = Product.objects.filter().order_by('-time')[:12]
    return render(request, "common/category.html", {
        "category" : category,
        "products": products,
        "recent_products": recent_products,
        "search": False,
    }
)

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']        
        
        message = f"Adı: {name}\nE-posta: {email}\nMesaj: {message}"
        
        mail.send_email(subject, message, "niyaziahmet.metin@tedu.edu.tr")
        # mail.send_email(subject, message, "burak.bilgi@tedu.edu.tr")
        
    return render(request, "common/contact.html")
