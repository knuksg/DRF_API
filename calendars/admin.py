from django.contrib import admin
from .models import CalendarEvent

@admin.register(CalendarEvent)
class CalendarEventAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'start', 'end', 'user']
    list_filter = ['user']
    search_fields = ['title', 'user__email']
    # date_hierarchy = 'start'
    ordering = ['start']