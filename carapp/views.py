from rest_framework import viewsets
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Count

from .models import Order, Color, Model, Brand
from carapp import serializers


''' Заказы на авто'''
class OrderAPIListPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10_000


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = serializers.DetailOrderSerializer


class OrderView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = serializers.OrderSerializer
    # Настройка фильтров
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields  = ('count', )
    filterset_fields = ['model__brand',]
    pagination_class = OrderAPIListPagination


''' Цвет авто'''
class ColorViewSet(viewsets.ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = serializers.ColorSerializer


class ColorTotalView(viewsets.ModelViewSet):
    queryset = Order.objects.all().values('color').annotate(total=Count('color'))
    serializer_class = serializers.ColorTotalSerializer


''' Модель авто'''
class ModelViewSet(viewsets.ModelViewSet):
    queryset = Model.objects.all()
    serializer_class = serializers.ModelSerializer


''' Бренд авто'''
class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = serializers.BrandSerializer


class BrandTotalView(viewsets.ModelViewSet):
    queryset = Order.objects.all().values('model__brand').annotate(total=Count('model__brand'))
    serializer_class = serializers.BrandTotalSerializer
