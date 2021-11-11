# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

# Internal:
from .models import OrderLineItem
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on lineitem update/create
    Args:
        sender (object): Sender object
        instance: Instance object
        created: created
        **kwargs: **kwargs
    Returns:
        N/A
    """
    instance.order.update_total()


@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update order total on lineitem delete
        Args:
        sender (object): Sender object
        instance: Instance object
        **kwargs: **kwargs
    Returns:
        N/A
    """
    instance.order.update_total()
