from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/beacon/(?P<user_id>\w+)/$', consumers.BeaconConsumer.as_asgi()),
]