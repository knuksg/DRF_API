from django.shortcuts import render
from .models import MbtiQuestion
from .serializers import MbtiQuestionSerializer
from rest_framework import viewsets

# Create your views here.


class MbtiView(viewsets.ModelViewSet):
    queryset = MbtiQuestion.objects.order_by('?')[:3]
    serializer_class = MbtiQuestionSerializer
