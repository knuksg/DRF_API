# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .models import User, Conversation
from .serializers import ConversationSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
import json

# Create your views here.
# @login_required
@csrf_exempt
def chatgpt(request, user_email):
    user = User.objects.get(email=user_email)
    conversation, created = Conversation.objects.get_or_create(user=user)

    if request.method == 'GET':
        # 대화 조회
        serializer = ConversationSerializer(conversation)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        # 대화 생성
        data = JSONParser().parse(request)
        serializer = ConversationSerializer(data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'PUT':
        # 대화 추가
        data = JSONParser().parse(request)
        conversation.conversation += '\n' + data['conversation']
        conversation.save()
        serializer = ConversationSerializer(conversation)
        return JsonResponse(serializer.data, status=200)