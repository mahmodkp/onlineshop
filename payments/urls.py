from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    PaymentReportViewSet,
    PaymentViewSet, 
)

app_name = "payments"

router = DefaultRouter()
router.register(r"pay", PaymentViewSet)
router.register(r"report", PaymentReportViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
