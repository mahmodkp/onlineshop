from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    PaymentViewSet, ReportViewSet
)

app_name = "payments"

router = DefaultRouter()
router.register(r"", PaymentViewSet)
router.register(r"report/", ReportViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
