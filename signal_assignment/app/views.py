import time
import threading
from django.db import transaction
from django.shortcuts import HttpResponse
from .models import TestModel

# Check if the signals are executed synchronously or not. It checks if the signal runs in the same thread as the caller or not.
def test_view(request):
    print("Before save")
    start_time = time.time()

    # This will trigger the post_save signal
    with transaction.atomic():
        obj = TestModel.objects.create(name="Test Object")
        print("After save, before transaction commit")

    end_time = time.time()
    total_time = end_time - start_time

    # print(f"After save, total time: {total_time} seconds")
    # print(f"View thread: {threading.current_thread().name}")

    return HttpResponse(f"Total time taken: {total_time} seconds")