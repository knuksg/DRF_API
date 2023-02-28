from rest_framework import serializers
from .models import CalendarEvent

class CalendaarEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalendarEvent
        fields = ('id', 'user', 'title', 'start', 'end', 'isAllDay', 'noti',)