from rest_framework import generics
from django_filters import rest_framework as filters
from blog.models import Article


class ArticleFilter(filters.FilterSet):
    # min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    # max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')

    class Meta:
        model = Article
        fields = {
            'category': ['exact'],
            #'created_at' : ['gt','lt'],
        }
    # min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    # max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')

    # class Meta:
    #     model = Product
    #     fields = ['category', 'in_stock']
