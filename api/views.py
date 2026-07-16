from django.shortcuts import render
from .models import Product
from rest_framework import viewsets
from .serializers import ProductSerializers
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView
# Create your views here.

class ProductListAPIView(ListAPIView):
    queryset= Product.objects.all()
    serializer_class= ProductSerializers

class ProductCreateAPIView(CreateAPIView):
    queryset= Product.objects.all()
    serializer_class= ProductSerializers

class ProductRetrieveAPIView(RetrieveAPIView):
    queryset= Product.objects.all()
    serializer_class= ProductSerializers

class ProductUpdateAPIView(UpdateAPIView):
    queryset= Product.objects.all()
    serializer_class= ProductSerializers

class ProductDestroyAPIView(DestroyAPIView):
    queryset= Product.objects.all()
    serializer_class= ProductSerializers

class ProductRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset= Product.objects.all()
    serializer_class= ProductSerializers

class ProductRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    queryset= Product.objects.all()
    serializer_class= ProductSerializers

class ProductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset= Product.objects.all()
    serializer_class= ProductSerializers

