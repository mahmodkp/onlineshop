from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Card, Invoice
from .service import send_mail_invoice


@receiver(post_save, sender=Card)
def send(sender, instance, created, **kwargs):
    if instance.paid:
        invoice = Invoice.objects.create(
            user=sender.user,
            card=sender)
        send_mail_invoice(invoice)
