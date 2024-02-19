from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied

from orders.models import Card, CardItem


class CardItemSerializer2(serializers.ModelSerializer):
    class Meta:
        model = CardItem
        fields = '__all__'


class CardItemSerializer(serializers.ModelSerializer):
    """
    Serializer class for serializing order items
    """

    price = serializers.SerializerMethodField()
    cost = serializers.SerializerMethodField()

    class Meta:
        model = CardItem
        fields = (
            "id",
            # "card",
            "product",
            "quantity",
            "price",
            "cost",
            # "created_at",
            # "updated_at",
        )
        read_only_fields = ("card",)

    def validate(self, validated_data):
        order_quantity = validated_data["quantity"]
        product_quantity = validated_data["product"].quantity
        # order_id = self.context["view"].kwargs.get("order_id")
        # product = validated_data["product"]
        # current_item = OrderItem.objects.filter(
        #     order__id=order_id,
        #     product=product
        # )

        if order_quantity > product_quantity:
            error = {"quantity": _("Ordered quantity is more than the stock.")}
            raise serializers.ValidationError(error)

        # if not self.instance and current_item.count() > 0:
        #     error = {"product": _("Product already exists in your order.")}
        #     raise serializers.ValidationError(error)

        # if self.context["request"].user == product.seller:
        #     error = _("Adding your own product to your order is not allowed")
        #     raise PermissionDenied(error)

        return validated_data

    def get_price(self, obj):
        return obj.product.price

    def get_cost(self, obj):
        return obj.cost


class CardReadSerializer(serializers.ModelSerializer):
    """
    Serializer class for reading orders
    """

    buyer = serializers.CharField(source="buyer.get_full_name", read_only=True)
    card_items = CardItemSerializer(many=True)
    total_cost = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Card
        fields = (
            "id",
            "buyer",
            "checkout_id",
            "paid",
            # "payment",
            "card_items",
            "total_cost",
            # "status",
            "created_at",
            "updated_at",
        )

    def get_total_cost(self, obj):
        return obj.total_cost


class CardWriteSerializer(serializers.ModelSerializer):
    """
    Serializer class for creating orders and order items

    Shipping address, billing address and payment are not included here
    They will be created/updated on checkout
    """

    # buyer = serializers.HiddenField(default=serializers.CurrentUserDefault())
    card_items = CardItemSerializer(many=True)

    class Meta:
        model = Card
        fields = (
            # "id",
            # "buyer",
            # "status",
            "card_items",
            # "product"
        )
        # read_only_fields = ("status",)

    def create(self, validated_data):
        # orders_data = validated_data.pop("order_items")
        user = self.context['user']
        last_card = Card.objects.filter(
            buyer=user).filter(paid=False).first()
        if last_card is None:
            last_card = Card.objects.create(buyer=user)
        card_products = CardItem.objects.filter(
            card=last_card).values_list('product', flat=True)
        for item in validated_data.pop("card_items"):    # validated_data['']
            product = item["product"]
            if product.id in card_products:
                print('hass')
                card_item = CardItem.objects.filter(
                    card=last_card).filter(product=product).first()
                card_item.quantity += item["quantity"]
                card_item.save()
            else:
                CardItem.objects.create(card=last_card, **item)
        return last_card

    def update(self, instance, validated_data):
        # # orders_data = validated_data.pop("order_items")
        # user = self.context['user']
        # last_card = Card.objects.filter(
        #     buyer=user).filter(paid=False).first()
        # # if last_card is None:
        # #     last_card = Card.objects.create(buyer=user)
        # card_products = CardItem.objects.filter(
        #     card=last_card).values_list('product', flat=True)
        # for item in validated_data.pop("card_items"):    # validated_data['']
        #     product = item["product"]
        #     if product.id in card_products:
        #         card_item = CardItem.objects.filter(
        #             card=last_card).filter(product=product).first()
        #         card_item.quantity = item["quantity"]
        #         if card_item.quantity == 0:
        #             card_item.delete()
        #         else:
        #             card_item.save()
        # return last_card
        items_data = validated_data.pop("card_items", None)
        items = list((instance.card_items).all())

        if items_data:
            for item in items_data:
                cartitem = items.pop(0)
                cartitem.product = item.get("product", cartitem.product)
                cartitem.quantity = item.get("quantity", cartitem.quantity)
                cartitem.save()

        return instance


# {
#     "card_items": [
#         {
#             "product": 3,
#             "quantity": 1
#         }
#     ]
# }
