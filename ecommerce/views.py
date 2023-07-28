# flake8: noqa
# from django.shortcuts import render
from rest_framework import viewsets
from .models import UserAccount, Product, Sale, Category
from .serializers import UserSerializer, ProductSerializer, SaleSerializer, CategorySerializer

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = UserAccount.objects.all()
    serializer_class = UserSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer