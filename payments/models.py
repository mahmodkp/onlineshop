from django.db import models
from django.utils.translation import gettext_lazy as _
from orders.models import Card


class Payment(models.Model):
    card = models.ForeignKey(
        Card,
        verbose_name=_("Customer Payment"),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    transaction_id = models.CharField(max_length=255)
    approved = models.BooleanField(default=False, verbose_name=("Paid"))
    timestamp = models.DateTimeField(auto_now_add=True)
    comment = models.CharField(verbose_name=(
        "Payment Comment"), max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Payment of customer: \
            {self.buyer.get_full_name()} for order: {self.card.id}"


