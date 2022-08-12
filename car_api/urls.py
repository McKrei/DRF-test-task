from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .yasg import urlpatterns as doc_url
from carapp import views
from carapp.routers import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/order/', views.OrderView.as_view({'get': 'list'})),
    path('api/v1/color/', views.ColorTotalView.as_view({'get': 'list'})),
    path('api/v1/brand/', views.BrandTotalView.as_view({'get': 'list'})),
    path('api/v1/', include(router.urls)),

]

urlpatterns += doc_url
