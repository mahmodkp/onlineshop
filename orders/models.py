from django.db import models
from django.contrib.auth import get_user_model
from django.utils.functional import cached_property
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from products.models import Product

User = get_user_model()

# Create your models here.


class Card(models.Model):
    buyer = models.ForeignKey(
        User , on_delete=models.CASCADE, related_name="customers"
    )
    checkout_id = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Checkout ID"
    )
    paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @cached_property
    def total_cost(self):
        """
        Total cost of all the items in an order
        """
        return round(sum([order_item.cost for order_item in self.order_items.all()]), 2)

    def __str__(self):
        return f"Customer: {self.buyer.first_name} {self.buyer.last_name} Order: {self.id} | Amount: {self.amount} Paid: {self.paid}"

    class Meta:
        verbose_name_plural = "Customer Cards"
        ordering = ("-created_at",)


class CardItem(models.Model):
    card = models.ForeignKey(
        Card, related_name="card_items", on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product, related_name="product_cards", on_delete=models.CASCADE
    )
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.card.buyer.get_full_name()

    @cached_property
    def cost(self):
        """
        Total cost of the ordered item
        """
        return round(self.quantity * self.product.price, 2)


class Invoice(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="invoices",
        null=True,
        blank=True,
    )
    card = models.ForeignKey(
        Card,
        verbose_name=_("Customer Order"),
        on_delete=models.CASCADE,
        related_name="invoices",
        null=True,
        blank=True,
    )
    invoice_number = models.IntegerField(
        verbose_name=_("Invoice Number"), null=True, blank=True, unique=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.invoice_number
