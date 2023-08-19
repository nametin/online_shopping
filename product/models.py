from django.db import models

# Create your models here.
class Product(models.Model):
    id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=300)
    image_url = models.URLField(max_length=500, default="")

    def __str__(self):
        return self.product_name