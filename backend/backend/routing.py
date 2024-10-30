# your_app/routing.py
from django.urls import re_path
from api.consumers import ConsumerCls

websocket_urlpatterns = [
    re_path(r'ws/socket-server/', ConsumerCls.as_asgi()),
]
