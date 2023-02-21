# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import User
from .serializers import UserSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
import json

# Create your views here.
@csrf_exempt
def account(request):
    if request.method == 'GET':
        # 전체 회원 조회
        query_set = User.objects.all()
        serializer = UserSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        print(1)
        # 회원 가입
        data = JSONParser().parse(request)
        data['mbti'] = None
        print(data)
        serializer = UserSerializer(data=data, partial=True)
        print(serializer)
        if serializer.is_valid():
            print('4')
            serializer.save()
            print('5')
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def account_detail(request, user_email):
    user = User.objects.get(email=user_email)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserSerializer(user, data=data, partial=True)
        if serializer.is_valid():
            print('success!')
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        user.delete()
        return HttpResponse(status=204)