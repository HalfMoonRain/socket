# urls.py
from django.urls import path
from .views import redis_test_view

urlpatterns = [
    path('redis-test/', redis_test_view),
]
