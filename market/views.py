#from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSeliarizer



# Create your views here.
@api_view(['GET'])

def get_user(request):
    users = User.objects.all()
    serializer =UserSeliarizer(users, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_user(request):
    serializer = UserSeliarizer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
    try:
        users = User.objects.get(pk=pk)   
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)    
    
    if request.method == 'GET':
         serializer = UserSeliarizer(users)
         return Response(serializer.data)
     
    elif request.method == 'PUT':
        serializer = UserSeliarizer(users, data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        users.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
        