from product.models import Product

def categories(request):
    categories = Product.objects.values('category').distinct()
    return {'categories': categories}