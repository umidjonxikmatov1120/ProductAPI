from django.contrib import admin

from products.models import ProductsModel, BrandModel

admin.site.register(ProductsModel)
admin.site.register(BrandModel)
