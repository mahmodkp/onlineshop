from django.urls import include, path
from rest_framework.routers import DefaultRouter

from products.views import (
    CategoryViewSet,
    ProductViewSet,
    CommentViewSet,
    ImagegalleryViewSet,
    VideogalleryViewSet,
)

app_name = "products"

router = DefaultRouter()
router.register(r"product", ProductViewSet)
router.register(r"categories", CategoryViewSet)
router.register(r"comments", CommentViewSet)
router.register(r"imagegallery", ImagegalleryViewSet)
router.register(r"videogallery", VideogalleryViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
