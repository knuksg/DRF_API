from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from .models import User

from .models import CalendarEvent
from .serializers import CalendaarEventSerializer

@api_view(['GET', 'POST'])
def event_list(request, user_email):
    user = User.objects.get(email=user_email)
    if request.method == 'GET':
        print(user)
        events = CalendarEvent.objects.filter(user=user)
        serializer = CalendaarEventSerializer(events, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        data['user'] = user.pk
        print(data)
        serializer = CalendaarEventSerializer(data=data)
        print('2')
        if serializer.is_valid():
            print('3')
            serializer.save()
            print('4')
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def event_detail(request, user_email, pk):

    user = User.objects.get(email=user_email)

    try:
        event = CalendarEvent.objects.get(pk=pk, user=user)
    except CalendarEvent.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CalendaarEventSerializer(event)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        data['user'] = user.pk
        serializer = CalendaarEventSerializer(event, data=data)
        if serializer.is_valid():
            print('test6')
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
