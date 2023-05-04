from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('aws/<str:root_name>/', consumers.MyAsyncJsonWebsocketConsumer.as_asgi()),
    # path('aws/', consumers.MyAsyncJsonWebsocketConsumer.as_asgi()),
]