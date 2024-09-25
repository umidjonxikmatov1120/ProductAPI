from rest_framework import generics
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from products.models import ProductsModel
from products.serializers import ProductsSerializer, ProductsViewSerializer


class ProductsListView(APIView):

    def get(self, request):
        products = ProductsModel.objects.all()
        serializers_data = ProductsSerializer(products, many=True).data
        data = {
            "status": f"{len(products)} ta produkt mavjud.",
            "products": serializers_data
        }

        return Response(data)


class ProductsCreateView(generics.CreateAPIView):
    queryset = ProductsModel.objects.all()
    serializer_class = ProductsViewSerializer


class ProductsUpdateView(generics.UpdateAPIView):
    queryset = ProductsModel.objects.all()
    serializer_class = ProductsViewSerializer


class ProductsRetrieveView(generics.RetrieveAPIView):
    queryset = ProductsModel.objects.all()
    serializer_class = ProductsViewSerializer

class ProductsDeleteView(generics.DestroyAPIView):
    queryset = ProductsModel.objects.all()
    serializer_class = ProductsViewSerializer
