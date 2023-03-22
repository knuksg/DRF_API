# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .models import User
from .serializers import UserSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
import json

# Create your views here.
@login_required
@csrf_exempt
def account(request):
    if request.method == 'GET':

        if not request.user.is_staff:
            raise PermissionDenied

        # 전체 회원 조회
        query_set = User.objects.all()
        serializer = UserSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        # 회원 가입
        data = JSONParser().parse(request)
        print(data)
        serializer = UserSerializer(data=data, partial=True)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@login_required
@csrf_exempt
def account_detail(request, user_email):
    user = User.objects.get(email=user_email)

    if user.email == request.user.email:
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
            if user.email == request.user.email:
                user.delete()
                return HttpResponse(status=204)
    else:
        return JsonResponse({'error': 'You do not have permission to perform this action.'}, status=403)