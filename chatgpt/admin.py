from django.contrib import admin
from .models import Conversation

class MessageInline(admin.StackedInline):
    model = Conversation
    extra = 0

class ConversationAdmin(admin.ModelAdmin):
    inlines = [MessageInline]
    list_display = ('user', 'created_at', 'updated_at')
    search_fields = ['user__username', 'Conversation__conversation']

admin.site.register(Conversation, ConversationAdmin)
