from rest_framework import generics, viewsets # v1
from rest_framework.generics import get_object_or_404 #v1

from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer


class CategoriesAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductsAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        if self.kwargs.get('categoria_pk'):
            return self.queryset.filter(category_id=self.kwargs.get('categoria_pk'))
        
        return self.queryset.all()


class ProductAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
