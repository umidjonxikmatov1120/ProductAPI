from django.db import models

class BrandModel(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class ProductsModel(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=100)
    image = models.URLField()
    size = models.CharField(max_length=10)
    brand = models.ForeignKey(BrandModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.title