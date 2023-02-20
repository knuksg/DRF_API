from django.urls import path, include
from . import views

urlpatterns = [
    path('events/<str:user_email>/', views.event_list),
    path('events/<str:user_email>/<int:pk>/', views.event_detail),
]