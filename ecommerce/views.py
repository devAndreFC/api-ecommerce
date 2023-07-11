from rest_framework import generics, viewsets 
from rest_framework.generics import get_object_or_404 
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from django.db.models import Q

from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer


class CategoriesAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductFilter(filters.FilterSet):
    search = filters.CharFilter(
        method='custom_search',
        label='Pesquise por nome, descrição ou categoria do produto.'
        )

    def custom_search(self, queryset, name, value):
        queryset = queryset.filter(
            Q(name__icontains=value) | 
            Q(description__icontains=value) | 
            Q(category__name__icontains=value)
        )
        return queryset

    class Meta:
        model = Product
        fields = ['search']

class ProductsAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter

    
    def get_queryset(self):
        if self.kwargs.get('categoria_pk'):
            return self.queryset.filter(category_id=self.kwargs.get('categoria_pk'))
        
        return self.queryset.all()


class ProductAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
