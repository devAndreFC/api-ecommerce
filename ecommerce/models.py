from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, blank=False, unique=True)
    description = models.TextField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    stock = models.IntegerField(default=0)
    category = models.ForeignKey(Category, blank=True, on_delete=models.SET_NULL, null=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/')
