from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from .models import Card, CardItem
# from orders.permissions import (
#     IsOrderByBuyerOrAdmin,
#     IsOrderItemByBuyerOrAdmin,
#     IsOrderItemPending,
#     IsOrderPending,
# )
from .serializers import (
    CardItemSerializer,
    CardReadSerializer,
    CardWriteSerializer,
)


# class CardItemViewSet(viewsets.ModelViewSet):
#     """
#     CRUD order items that are associated with the current order id.
#     """

#     queryset = CardItem.objects.all()
#     serializer_class = CardItemSerializer
#    # permission_classes = [IsOrderItemByBuyerOrAdmin]

#     def get_queryset(self):
#         res = super().get_queryset()
#         order_id = self.kwargs.get("order_id")
#         return res.filter(order__id=order_id)

#     def perform_create(self, serializer):
#         order = get_object_or_404(Order, id=self.kwargs.get("order_id"))
#         serializer.save(order=order)

#     def get_permissions(self):
#         if self.action in ("create", "update", "partial_update", "destroy"):
#             self.permission_classes += [IsOrderItemPending]

#         return super().get_permissions()


class CardViewSet(viewsets.ModelViewSet):
    """
    CRUD orders of a Cart
    """
    queryset = Card.objects.all()
    # permission_classes = [IsOrderByBuyerOrAdmin]

    @action(detail=True, methods=["get"])
    def checkout(self, request, pk=None):
        order = self.get_object()
        pass

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
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

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

    # def get_permissions(self):
    #     if self.action in ("update", "partial_update", "destroy"):
    #         self.permission_classes += [IsOrderPending]

    #     return super().get_permissions()
