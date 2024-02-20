from rest_framework import generics
from django_filters import rest_framework as filters
from products.models import Product


class ProductFilter(filters.FilterSet):

    class Meta:
        model = Product
        fields = {
            'category': ['exact'],
            'price': ['gt', 'lt'],
            'quantity': ['gt'],
        }
    # min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    # max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')

    # class Meta:
    #     model = Product
    #     fields = ['category', 'in_stock']
