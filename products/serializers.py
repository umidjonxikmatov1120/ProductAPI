from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from products.models import ProductsModel


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductsModel
        fields = ('id', 'title', 'brand', 'image', 'price')


class ProductsViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductsModel
        fields = ('id', 'title', 'description', 'price', 'color', 'image', 'size', 'brand')


class ProductsValidateSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    color = serializers.CharField()
    image = serializers.URLField()
    size = serializers.CharField()
    brand = serializers.IntegerField()

    def validate(self, data):
        title = data.get('title', None)
        brand = data.get('brand', None)

        if ProductsModel.objects.filter(brand=brand, title=title).exists():
            raise ValidationError(
                {
                    'status': False,
                    'message': "Bunday brend yoki nom bor.Iltimos boshqa nom kiriting!"
                }
            )

        if not title.isalpha():
            raise ValidationError(
                {
                    "status": False,
                    "message": "Mahsulotni nomi harflardan tashkil topgan bo'lshi kerak !"
                }
            )
        return data


    def validate_price(self, price):
        if 0 < price < 10_000_000_000:
            raise ValueError(
                {
                    'status': False,
                    'message': "Narx noto'g'ri kiritilgan"
                }
            )

