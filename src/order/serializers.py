from rest_framework import serializers
from .models import Order , OrderAPIView

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OrderAPIViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderAPIView
        fields = '__all__'

class GetOrderSerializer(serializers.Serializer):
    orderId1 = serializers.CharField(max_length=200)
    total_price1 = serializers.CharField(max_length=200)
    orderName1 = serializers.CharField(max_length=200)
