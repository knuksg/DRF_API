from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path('', views.account),
    path('<str:user_email>/', views.account_detail),
]
