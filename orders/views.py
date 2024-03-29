# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.decorators import action
from .models import Card
from .serializers import (
    CardReadSerializer,
    CardWriteSerializer,
)


class CardViewSet(viewsets.ModelViewSet):
    """
    CRUD orders of a Cart
    """
    queryset = Card.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    @action(detail=True, methods=["get"])
    def checkout(self, request, pk=None):
        """
        Order Checkout for payment
        """
        card = Card.objects.filter(id=pk).first()
        if not card:
            return Response(status=status.HTTP_204_NO_CONTENT)
        if card.buyer != self.request.user:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        for item in card.card_items:
            if item.quantity > card.product.quantity:
                return Response({
                    'Checkout error': 'Product quantity in shopping cart \
                        is graeter than product quantity'
                },
                    status=status.HTTP_400_BAD_REQUEST)
        # TODO: Create a checkout id and send checkout id and amount to gateway
        return Response(status=status.HTTP_200_OK)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.filter(buyer=self.request.user).filter(paid=False)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={
                                         'user': self.request.user})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED,
                        headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial, context={
                'user': self.request.user})
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def get_serializer_class(self):
        if self.action in ("create", "update", "partial_update", "destroy"):
            return CardWriteSerializer
        return CardReadSerializer

    def get_queryset(self):
        res = super().get_queryset()
        user = self.request.user
        return res.filter(buyer=user)


class CardReportViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Card.objects.all()
    serializer_class = CardReadSerializer
    permission_classes = (
        permissions.IsAdminUser,
    )
