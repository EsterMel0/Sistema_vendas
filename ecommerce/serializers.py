from rest_framework import serializers
from .models import UserAccount, Product, Sale, Category


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserAccount
        exclude = ''


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        exclude = ''


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        exclude = ''


class SaleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sale
        exclude = ''
