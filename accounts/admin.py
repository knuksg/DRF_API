from django.contrib import admin
from .models import User
from .serializers import UserSerializer

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'gender', 'birthday', 'height', 'weight', 'mbti')
    search_fields = ('username', 'email',)
    list_filter = ('gender', 'mbti',)
    ordering = ('-id',)

    def get_serializer(self, request):
        return UserSerializer

admin.site.register(User, UserAdmin)