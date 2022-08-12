from rest_framework import serializers
from .models import Order, Model, Color, Brand


class OrderSerializer(serializers.ModelSerializer):
    ''' Serializer для отображения списка, добавляем бренд автомобиля '''
    brand = serializers.CharField(max_length=256, source='model.brand')

    class Meta:
        model = Order
        fields = ('date', 'color', 'brand', 'model', 'count')


class DetailOrderSerializer(serializers.ModelSerializer):
    ''' Стандартный Serializer CRUD  Заказов '''
    class Meta:
        model = Order
        fields = '__all__'


class ColorSerializer(serializers.ModelSerializer):
    ''' Стандартный Serializer CRUD  Цветов '''
    class Meta:
        model = Color
        fields = '__all__'


class ColorTotalSerializer(serializers.Serializer):
    ''' Serializer для отображения списка цветов и количества заказов '''
    color = serializers.CharField(max_length=256)
    total = serializers.IntegerField()


class ModelSerializer(serializers.ModelSerializer):
    ''' Стандартный Serializer CRUD  Цветов '''
    class Meta:
        model = Model
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    ''' Стандартный Serializer CRUD  Цветов '''
    class Meta:
        model = Brand
        fields = '__all__'


class BrandTotalSerializer(serializers.Serializer):
    ''' Serializer для отображения списка Брендов и количества заказов '''
    model__brand = serializers.CharField(max_length=256)
    total = serializers.IntegerField()
