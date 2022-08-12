from rest_framework import routers

from carapp.views import OrderViewSet, ColorViewSet, ModelViewSet, BrandViewSet


''' Создаем роутеры '''
router = routers.DefaultRouter()
router.register(r'order', OrderViewSet, basename='order')
router.register(r'color', ColorViewSet, basename='color')
router.register(r'model', ModelViewSet, basename='model')
router.register(r'brand', BrandViewSet, basename='brand')
    