from django.urls import include, path
from rest_framework.routers import DefaultRouter

from orders.views import CardReportViewSet, CardViewSet

app_name = "orders"

router = DefaultRouter()
router.register(r"card", CardViewSet)
router.register(r"report", CardReportViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
