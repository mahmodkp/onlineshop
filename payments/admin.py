from django.contrib import admin


# Register your models here.

from .models import (
    Payment,
)


# Category admin page
class PaymentAdmin(admin.ModelAdmin):
    list_display = [
        "card",
        "transaction_id",
        "approved",
        "created_at",
    ]

    list_filter = ["approved"]
    list_per_page = 30

    def is_active(self, instance):
        return instance.is_active()


admin.site.register(Payment, PaymentAdmin)