from django.conf import settings
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters import rest_framework as filters
from payments.models import Payment
from .serializers import  PaymentSerializer
from rest_framework import permissions
from .services import send_email,send_invoice_email
from rest_framework import generics, mixins, views
from rest_framework.decorators import action
class PaymentViewSet(ModelViewSet):
    """
    CRUD payment for an Payment
    """
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    # get payment status
    @action(detail=True, methods=["get"])
    def payment(self, request, pk=None):
        pass

    # def get_queryset(self):
    #     res = super().get_queryset()
    #     user = self.request.user
    #     return res.filter(card__buyer=user)

    def get_permissions(self):
        if self.action in ("update", "partial_update", "destroy"):
            permission_classes = (permissions.IsAuthenticated,)

        return super().get_permissions()


class ReportViewSet(ReadOnlyModelViewSet):
   
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    # permission_classes = (permissions.IsAdminUser,)
    # filter_backends = (filters.DjangoFilterBackend,
    #                    SearchFilter, OrderingFilter)
    # search_fields = ['title', 'text', 'category__name']
    # ordering_fields = ['created_at']
    # filterset_class = ArticleFilter  # ('category',)
    # def get_queryset(self):
    #     res = super().get_queryset()
    #     user = self.request.user
    #     return res.filter(card__buyer=user)

    # def get_permissions(self):
    #     if self.action in ("update", "partial_update", "destroy"):
    #         permission_classes = (permissions.IsAuthenticated,)

    #     return super().get_permissions()
