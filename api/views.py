from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializers
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
# Create your views here.

@api_view(["GET"])
def ProductListView(request):
    products=Product.objects.all()
    serializer = ProductSerializers(products, many=True)
    return Response(serializer.data)

@api_view(["GET","POST"])
def product_create(request):
    if request.method == "GET":
        return Response({"message":"POST request yuborn"})
    serializer = ProductSerializers(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def ProductDetailView(request, pk):
    products=Product.objects.get(pk=pk)
    serializer = ProductSerializers(products)
    return Response(serializer.data)


@api_view(["PUT","PATCH"])
def product_update(request,pk):
    products=Product.objects.get(pk=pk)
    if request.method == "PUT":
        serializer = ProductSerializers(products,data = request.data)
    else:
        serializer = ProductSerializers(products,data = request.data, partial=True)
        
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def product_delete(request, pk):
    products=Product.objects.get(pk=pk)
    products.delete()
    return Response({"message":"product ochirildi"}, status=status.HTTP_204_NO_CONTENT)