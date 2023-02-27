from django.db import models
from accounts.models import User

# Create your models here.
class CalendarEvent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    start = models.DateTimeField()
    end = models.DateTimeField()
    isAllDay = models.BooleanField()

    def __str__(self):
        return self.title