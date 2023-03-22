from django.contrib import admin
from .models import Conversation, Message

class MessageInline(admin.StackedInline):
    model = Message
    extra = 0

class ConversationAdmin(admin.ModelAdmin):
    inlines = [MessageInline]
    list_display = ('user', 'created_at', 'updated_at')
    search_fields = ['user__username', 'messages__content']

admin.site.register(Conversation, ConversationAdmin)
