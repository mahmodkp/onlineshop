from rest_framework import (
    status,
    viewsets,
    permissions,
)
from rest_framework.response import Response
from rest_framework.viewsets import (
    GenericViewSet,
    mixins,
)
from orders.models import Card
from payments.models import Payment
from .serializers import PaymentSerializer
import datetime


class PaymentViewSet(mixins.ListModelMixin,
                     GenericViewSet):
    """
    CRUD payment call Back
    """
    http_method_names = ['get']
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def list(self, request, *args, **kwargs):
        """
        The callback function for payment gateway.
        """
        transaction_id = '12'
        timestamp = datetime.datetime.now
        card = Card.objects.filter(checkout_id=transaction_id).first()
        data = {
            "card": card.id,
            "transaction_id": transaction_id,
            "timestamp": timestamp,
            "comment": 'ok',
            "approved": True,
        }
        serializer = PaymentSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)


class PaymentReportViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = (
        permissions.IsAdminUser,
    )
