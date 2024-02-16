from django.contrib import admin

# Register your models here.
from orders.models import Card, CardItem, Invoice

admin.site.register(Card)
admin.site.register(CardItem)
admin.site.register(Invoice)

