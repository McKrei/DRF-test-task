from django.contrib import admin

# Register your models here.
from .models import Order, Color, Model, Brand


admin.site.register(Order)
admin.site.register(Color)
admin.site.register(Model)
admin.site.register(Brand)
