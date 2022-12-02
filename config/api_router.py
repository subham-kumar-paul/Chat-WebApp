from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from chat_dj.users.api.views import UserViewSet
from chat_dj.chats.api.views import ConversationViewSet
from chat_dj.chats.api.views import MessageViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register('conversations', ConversationViewSet)
router.register("messages", MessageViewSet)


app_name = "api"
urlpatterns = router.urls
