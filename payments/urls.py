from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    PaymentViewSet,
)

app_name = "payments"

router = DefaultRouter()
router.register(r"", PaymentViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
