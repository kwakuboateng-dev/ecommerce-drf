from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response   

from .models import Category
from .serializers import CategorySerializer


class CategoryViewSet(viewsets.ViewSet):
    """
    A viewset for viewing category instances.   
    """
    queryset = Category.objects.all()
    
    def list(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)
