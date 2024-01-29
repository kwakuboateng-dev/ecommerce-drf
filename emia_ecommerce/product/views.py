from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response   
from drf_spectacular.utils import extend_schema

from .models import Category, Brand
from .serializers import CategorySerializer, BrandSerializer


class CategoryViewSet(viewsets.ViewSet):
    """
    A viewset for viewing category instances.   
    """
    queryset = Category.objects.all()
    
    @extend_schema(responses=CategorySerializer)
    def list(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)
    

class BrandViewSet(viewsets.ViewSet):
    """
    A viewset for viewing category brands.   
    """
    queryset = Category.objects.all()
    
    @extend_schema(responses=BrandSerializer)
    def list(self, request):
        queryset = Brand.objects.all()
        serializer = BrandSerializer(queryset, many=True)
        return Response(serializer.data)
