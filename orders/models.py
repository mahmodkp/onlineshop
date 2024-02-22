from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _
from products.models import Product

User = get_user_model()


class Card(models.Model):
    """
    The shoping cards models
    """
    buyer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="customers"
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
        return round(
            sum([order_item.cost for order_item in self.card_items.all()]), 2)

    def __str__(self):
        return f"Customer: {self.buyer.get_full_name()}, Order: {self.id},\
                Amount: {self.total_cost}, Paid: {self.paid}"

    class Meta:
        verbose_name_plural = "Customer Carts"
        ordering = ("-created_at",)


class CardItem(models.Model):
    """
    The shoping cards items models to save the items of product in
    eacch shoping cart
    """
    card = models.ForeignKey(
        Card, related_name="card_items", on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product, related_name="product_cards", on_delete=models.CASCADE
    )
    quantity = models.IntegerField(validators=[MinValueValidator(0)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.card.buyer.get_full_name()

    @cached_property
    def cost(self):
        """
        Cost calculation for each cart item
        """
        return round(self.quantity * self.product.price, 2)


class Invoice(models.Model):
    """
    The Invoce model to save the invoices of success paymments
    """
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

    def save(self, *args, **kwargs):
        invoices = Invoice.objects.all()

        if invoices.exists() and self._state.adding:
            last_invice = invoices.latest()
            self.invoice_number = int(last_invice.order) + 1
        else:
            self.invoice_number = 1000
        super().save(*args, **kwargs)
