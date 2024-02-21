from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet, GenericViewSet,mixins
from orders.models import Card
from payments.models import Payment
from .serializers import  PaymentSerializer
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
            #"timestamp":timestamp,
            "comment":'ok',
            "approved": True,
        }
        serializer = PaymentSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)

    

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
