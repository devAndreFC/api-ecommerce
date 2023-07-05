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
