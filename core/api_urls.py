from rest_framework import routers
from rest_framework.routers import DefaultRouter
from market import views as market_views
from django.urls import include, path
router = DefaultRouter()

router.register('market', market_views.DSViewSet, basename='market')

#urlpatterns = router.urls
urlpatterns = [
    path("", include(router.urls)),
    path("market2/", market_views.DSView.as_view()),
]
