# signals.py
import time
import threading
from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import TestModel

@receiver(post_save, sender=TestModel)
def slow_signal_handler(**kwargs):
    print("Signal handler started")
    # time.sleep(5)  # Simulate a slow task (5 seconds delay)

    # print(f"Signal handler thread: {threading.current_thread().name}")

    # Check if the transaction is still active
    print(f"Transaction state: {transaction.get_connection().in_atomic_block}")

    print("Signal handler finished")
