from django.urls import include, path
from rest_framework.routers import DefaultRouter

from blog.views import (
    CategoryViewSet,
    ArtcleViewSet,
    CommentViewSet,
)

app_name = "blog"
router = DefaultRouter()
router.register(r"articles", ArtcleViewSet)
router.register(r"categories", CategoryViewSet)
router.register(r"comments", CommentViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
