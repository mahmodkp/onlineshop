
from django.contrib import admin
from orders.models import Card, CardItem, Invoice

# Category admin page


class CardAdmin(admin.ModelAdmin):
    """
    Admin panel for Card Model
    """
    list_display = [
        "buyer",
        "checkout_id",
        "paid",
    ]
    list_filter = ["paid"]
    list_editable = ["paid"]
    list_per_page = 30

    def is_active(self, instance):
        return instance.is_active()

# Product admin page


class CardItemAdmin(admin.ModelAdmin):
    """
    Admin panel for Card items Model
    """
    list_display = [
        "card",
        "product",
        "quantity",
    ]
    list_per_page = 30

    def is_active(self, instance):
        return instance.is_active()


class InvoiceAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "card",
        "invoice_number",

    ]
    list_per_page = 30

    def is_active(self, instance):
        return instance.is_active()


admin.site.register(Card, CardAdmin)
admin.site.register(CardItem, CardItemAdmin)
admin.site.register(Invoice, InvoiceAdmin)