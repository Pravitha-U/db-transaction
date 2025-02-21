from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse
from django.db import transaction
from .models import SampleModel


# def create_sample_model(request):
#     try:
#         with transaction.atomic():  # Start a transaction
#             sample = SampleModel.objects.create(name="Test")
#             print("Model saved, now signal should trigger")
#     except Exception as e:
#         return HttpResponse("Transaction Rolled Back:{}".format(e))
#
#     return HttpResponse("SampleModel instance created successfully")
def my_view(request):
    with transaction.atomic():
        sample=SampleModel.objects.create(name="test")
        return HttpResponse("Transaction active in view:{}".format(transaction.get_autocommit))