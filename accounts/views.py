from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import User
from .serializers import UserSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser

# Create your views here.
@csrf_exempt
def account(request):
    if request.method == 'GET':
        # 전체 회원 조회
        query_set = User.objects.all()
        serializer = UserSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        # 회원 가입
        data = JSONParser().parse(request)
        data['mbti'] = None
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def account_detail(request, user_email):
    obj = User.objects.get(email=user_email)

    if request.method == 'GET':
        serializer = UserSerializer(obj)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        print(request.PUT.get('email'))
        data['email'] = request.PUT.get('email')
        serializer = UserSerializer(obj, data=data)
        if serializer.is_valid():
            print('success!')
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        obj.delete()
        return HttpResponse(status=204)