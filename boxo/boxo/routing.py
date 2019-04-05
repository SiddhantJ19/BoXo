from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import file_sharing.routing

application = ProtocolTypeRouter({
'websocket':AuthMiddlewareStack(
	URLRouter(file_sharing.routing.websocket_urlpatterns)
	),
})
