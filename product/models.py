from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=300)
    time = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return f"id: {self.product_id} name : {self.product_name}"
    
class ProductImage(models.Model):
    product_id = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE,default="-1")
    image_url = models.URLField(max_length=500, default="")

    def __str__(self):
        return self.image_url