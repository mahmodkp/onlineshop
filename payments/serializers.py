from rest_framework import serializers

from .models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    """
    Serializer class for patyment
    """

    class Meta:
        model = Payment
        fields = "__all__"



