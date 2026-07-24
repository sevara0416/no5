from django.shortcuts import render
from .models import Product, CustomUser
from .serializers import ProductSerializer, RegisterSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
# Create your views here.

class RegisterAPIView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

class ProfileAPIView(APIView):
    permission_classes= [IsAuthenticated]
    def get(self, request):
        return Response({"usernama": request.user.username, "email":request.user.email,})

class LogoutAPIView(APIView):
    permission_classes=[IsAuthenticated]
    def product(self, request):
        try:
            refresh_token=request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message":"logout seccessfil"}, status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response({"error":"eee invalid bopqopti tokenin"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def ProductListView(request):
    products=Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(["GET","POST"])
def product_create(request):
    if request.method == "GET":
        return Response({"message":"POST request yuborn"})
    serializer = ProductSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def ProductDetailView(request, pk):
    products=Product.objects.get(pk=pk)
    serializer = ProductSerializer(products)
    return Response(serializer.data)


@api_view(["PUT","PATCH"])
def product_update(request,pk):
    products=Product.objects.get(pk=pk)
    if request.method == "PUT":
        serializer = ProductSerializer(products,data = request.data)
    else:
        serializer = ProductSerializer(products,data = request.data, partial=True)
        
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def product_delete(request, pk):
    products=Product.objects.get(pk=pk)
    products.delete()
    return Response({"message":"product ochirildi"}, status=status.HTTP_204_NO_CONTENT)