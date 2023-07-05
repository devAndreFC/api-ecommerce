from django.urls import path

from .views import CategoriesAPIView, CategoryAPIView

urlpatterns = [
    path('categorias/', CategoriesAPIView.as_view(), name='categorias'),
    path('categorias/<int:pk>/', CategoryAPIView.as_view(), name='categoria'),
]