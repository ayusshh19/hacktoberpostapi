from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from posthand.models import Postapi

from rest_framework import status
from posthand.serializers import Postserializers


# Create your views here.
@api_view(['GET'])
def home(request):
    if request.method=='GET':
        stu=Postapi.objects.all()
        serializer = Postserializers(stu, many=True)
        return Response(serializer.data)
    return Response({'data':'Invalid method'},status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def add_post(request):
    if request.method == 'POST':
        serializer = Postserializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Created'}
            return Response(res, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    return Response({'data':'Invalid method'},status=status.HTTP_204_NO_CONTENT)

