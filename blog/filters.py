from django_filters import rest_framework as filters
from blog.models import Article


class ArticleFilter(filters.FilterSet):
    """
    Filter an article based on Category and oter fields
    """
    class Meta:
        model = Article
        fields = {
            'category': ['exact'],
        }