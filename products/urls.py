from django.urls import include, path
from rest_framework.routers import DefaultRouter

from products.views import (
    CategoryViewSet,
    ProductViewSet,
    CommentViewSet,
)

app_name = "products"

router = DefaultRouter()
router.register(r"product", ProductViewSet)
router.register(r"categories", CategoryViewSet)
router.register(r"comments", CommentViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
