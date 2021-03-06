from time import time
from turtle import title
from django.db import models

# Create your models here.


class Order(models.Model):
    # thông tin mặc định - một order có thể có nhiều Line_Item_Order
    orderId = models.CharField(max_length=200,unique=True)  # orderId  same #AS-51898-US
    total_price = models.FloatField(default=0.0, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=False,null=True)
    city = models.CharField(max_length=50,null=False,blank=True)
    shop_site = models.CharField(max_length=50,null=True)
    number_line_item = models.IntegerField(default=1,null=False)

    def __str__(self):
            return self.orderId

class Line_Item_Order(models.Model):
    # thông tin mặc định
    line_item_order_id = models.CharField(max_length=200,unique=True)#nó thuộc về một order nào đấy duy nhất
    order = models.CharField(max_length=50,null=True)
    created_at = models.DateTimeField(auto_now_add=False,null=True)
    shop_site = models.CharField(max_length=50,null=True)
    fulfillment_status = models.CharField(max_length=50,blank=True, null=True)
    image_src = models.URLField(max_length=255)
    product_id = models.CharField(max_length=100)
    price = models.FloatField(default=0.0, blank=False, null=False)
    quantity = models.IntegerField(default=1,null=False , blank=False)
    sku = models.CharField(max_length=100,null=True)
    title = models.CharField(max_length=255)
    vendor = models.CharField(max_length=100)
    def __str__(self):
            return self.line_item_order_id

class OrderAPIView(models.Model):
    # thông tin mặc định
    orderId1 = models.CharField(max_length=200)
    total_price1 = models.FloatField(default=0.0, blank=True, null=True)
    orderName1 = models.CharField(max_length=200) # name order same #AS-51898-US


class DataModel(models.Model):
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255)