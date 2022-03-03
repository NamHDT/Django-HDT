from django.contrib import admin
from .models import Order, OrderAPIView, DataModel
# Register your models here.

admin.site.register(Order)
admin.site.register(OrderAPIView)
admin.site.register(DataModel)