from django.urls import path

from .views import (
    CategoriesAPIView, 
    CategoryAPIView, 
    ProductAPIView, 
    ProductsAPIView)


urlpatterns = [
    path('categorias/', CategoriesAPIView.as_view(), name='categorias'),
    path('categorias/<int:pk>/', CategoryAPIView.as_view(), name='categoria'),
    path('categorias/<int:categoria_pk>/produtos', ProductsAPIView.as_view(), name='categoria_produtos'),

    path('produtos/', ProductsAPIView.as_view(), name='produtos'),
    path('produtos/<int:pk>/', ProductAPIView.as_view(), name='produto'),
]