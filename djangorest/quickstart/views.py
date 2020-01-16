from django.shortcuts import render

from django.contrib.auth.models import User, Group
from .models import Merchant
from rest_framework import viewsets
from .serializers import MerchantSerializer, GroupSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

class MerchantViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows merchants to be viewed or edited
    '''
    queryset = Merchant.objects.all().order_by('-date_joined')
    serializer_class = MerchantSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

@api_view(['GET', 'POST'])
def merchant(request):
    if request.method == 'GET':
        merchant = Merchant.objects.all()
        serializer = UserSerializer(merchant)
        return Response(serializers.data)

    elif request.method == 'POST':
        serializer = MerchantSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request):
    try:
        merchant = Merchant.objects.get(pk=pk)
    except Merchant.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MerchantSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MerchantSerializer(user, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Resonse(serializer.errors, status=status.HTTP_404_BAD_REQUEST)

    elif request.method == 'DELETE':
        merchant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
