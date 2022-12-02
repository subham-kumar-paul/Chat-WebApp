from django.contrib import admin
from . models import Conversation, Message

# Register your models here.
@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'from_user', 'to_user', 'content', 'timestamp', 'read']