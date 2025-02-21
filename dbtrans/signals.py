from django.db.models.signals import post_save
from django.db import transaction
from django.dispatch import receiver
from .models import SampleModel

@receiver(post_save, sender=SampleModel)
def my_signal_handler(sender, instance, created, **kwargs):
    if created:
        # print("Signal Triggered: Checking transaction state...")
        # print("In atomic transaction:", transaction.get_connection().in_atomic_block)
        print("Signal Received-inside transaction:{}".format(transaction.get_autocommit))