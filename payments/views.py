from django.conf import settings
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from payments.models import Payment
from .serializers import  PaymentSerializer
from rest_framework import permissions
from .services import send_email,send_invoice_email


class PaymentViewSet(ModelViewSet):
    """
    CRUD payment for an Payment
    """
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    # def get_queryset(self):
    #     res = super().get_queryset()
    #     user = self.request.user
    #     return res.filter(card__buyer=user)

    def get_permissions(self):
        if self.action in ("update", "partial_update", "destroy"):
            permission_classes = (permissions.IsAuthenticated,)

        return super().get_permissions()
