from django.urls import include, path
from rest_framework.routers import DefaultRouter

from orders.views import CardViewSet

app_name = "orders"

router = DefaultRouter()
router.register(r"", CardViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
