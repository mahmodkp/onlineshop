from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Card
# TODO: Send Invoce mail for the buyer
# TODO: Send Notifications to buyer


@receiver(post_save, sender=Card)
def send(sender, instance, created, **kwargs):
    if instance.paid:

        pass
    return
