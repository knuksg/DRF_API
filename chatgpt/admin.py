from django.contrib import admin
from .models import Conversation

class ConversationAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ['user__username',]

admin.site.register(Conversation, ConversationAdmin)
