from django.urls import path
from .views import my_view

urlpatterns = [
    path('test-transaction/', my_view, name='test_transaction'),
]