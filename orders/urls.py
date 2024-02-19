from django.urls import include, path
from rest_framework.routers import DefaultRouter

from orders.views import CardViewSet  # CardItemViewSet,

app_name = "orders"

router = DefaultRouter()
#router.register(r"^(?P<order_id>\d+)/order-items", CardItemViewSet)
router.register(r"", CardViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
