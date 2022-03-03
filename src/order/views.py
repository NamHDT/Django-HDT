from turtle import title
from webbrowser import get
import requests
import json
from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Order, OrderAPIView, Line_Item_Order
from .serializers import OrderSerializer, OrderAPIViewSerializer, LineItemOrderSerializer, GetOrderSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
import datetime

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.filter()
    serializer_class = OrderSerializer
    # permission_classes = (permissions.IsAuthenticated)
    #list  (GET)
    #...(POST)
    #detail
    #...(PUT)
    #...(DELETE)
class LineItemOrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.filter()
    serializer_class = LineItemOrderSerializer

class GetAllOrderAPIView(APIView):
    def get(self, request):
        list_order = OrderAPIView.objects.all()
        mydata = OrderAPIViewSerializer(list_order, many = True)
        return Response(data=mydata.data, status=status.HTTP_200_OK)


    # def post(self, request):
    #     mydata = GetOrderSerializer(data=request.data)
    #     if not mydata.is_valid():
    #         return Response('sai lieu sai', status=status.HTTP_400_BAD_REQUEST)
    #     orderId = mydata.data['orderId1']
    #     total_price = mydata.data['total_price1']
    #     orderName = mydata.data['orderName1']
    #     cs = Order.objects.create(orderId=orderId,total_price=total_price,orderName=orderName)
    #     return Response(data=cs.id, status=status.HTTP_200_OK)



def index(request):
    #Order.objects.all().delete()
    #Line_Item_Order.objects.all().delete()
    # allData=[]
    # orderId=[]
    # total_price=[]
    # orderName=[]
    # sku=[]
    # res = requests.get("https://bcf351dba928d38aa14a084313104bbf:fe17f0728674c6cab25db9f6b522da2b59fb68660bf293c13596775af2927179@mysticlifee.onshopbase.com/admin/orders.json")
    # for item in (json.loads(res.text)['orders']):
    #     print(item['order_number'])
    #     orderId.append(item['name'])
    #     total_price.append(item['total_price'])
    #     orderName.append(item['line_items'][0]['title'])
    #     sku.append(item['line_items'][0]['sku'])

#### lấy dữ liệu  order từ  shopbase
    url_shopbase=[]
    url_shopbase.append("https://bcf351dba928d38aa14a084313104bbf:fe17f0728674c6cab25db9f6b522da2b59fb68660bf293c13596775af2927179@mysticlifee.onshopbase.com/admin/orders.json")
    url_shopbase.append("https://ae1c566c25bbabcbbc7c5176b1be07dc:6b5642a08755a48b143c5d1743a47210fea75605b34e459acf7a82805e7fa0ce@olafize.onshopbase.com/admin/orders.json")
    url_shopbase.append("https://693cd44a9f7cce289e7b44e9a17c61b7:cd12c08bc8eeeee69be8db3ae67b8543081fcb24527698c1520d9e96f0418341@mysticlif-com.onshopbase.com/admin/orders.json")
    #url_shopbase.append("https://b38ec5272c109c19db33f596ca9ab60c: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@trending-verse.myshopify.com/admin/api/2022-01/orders.json")
    # url.append("
    # url.append("    


    for site in url_shopbase:
        res = requests.get(site)
        for item in (json.loads(res.text)['orders']):
            orderId = item['name']
            #created_at = item['created_at_in_timezone']
            created_at = item['created_at']
            total_price = item['total_price']
            city = item['billing_address']['city']
            #Viết ra order thuộc website nào dựa vào link url hóa đơn của site (shopbase)
            invoice = item['invoice_url']
            dotstart = item['invoice_url'].find(".")
            dotend = item['invoice_url'].rfind(".")
            shop_site = invoice[(dotstart+1):dotend].upper()
            #
            number_line_item = len(item['line_items'])
            #tạo thêm order vào database
            try:
                Order.objects.update_or_create(
                    orderId=orderId,
                    total_price=total_price,
                    created_at=created_at,
                    city = city,
                    shop_site= shop_site,
                    number_line_item=number_line_item
                )
            except:
                print(orderId + " existed")
            for line_item in range(number_line_item):
                order       = orderId #  item['name']
                line_item_order_id = orderId+"__"+str(line_item)
                #shop_site   = shop_site
                fulfillment_status = item['line_items'][line_item]['fulfillment_status']
                image_src   = item['line_items'][line_item]['image_src']
                #created_at  = created_at]
                product_id  = item['line_items'][line_item]['product_id']
                price       = item['line_items'][line_item]['price']
                quantity    = item['line_items'][line_item]['quantity']
                sku         = item['line_items'][line_item]['sku']
                title       = item['line_items'][line_item]['title']
                vendor      = item['line_items'][line_item]['vendor']
                #tạo thêm line item order vào database
                try:
                    Line_Item_Order.objects.update_or_create(
                    line_item_order_id=line_item_order_id,
                    order=order,
                    shop_site=shop_site,
                    created_at=created_at,
                    fulfillment_status = fulfillment_status,
                    image_src=image_src,
                    product_id = product_id,
                    price = price,
                    quantity = quantity,
                    sku = sku,
                    title = title,
                    vendor = vendor,)
                except:
                    print(line_item_order_id+"existed")

####################################
#### lấy dữ liệu  order từ  shopify
    url_shopify=[]
    url_shopify.append("https://b38ec5272c109c19db33f596ca9ab60c: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@trending-verse.myshopify.com/admin/api/2022-01/")

    for site in url_shopify:
        res = requests.get(site+"orders.json")   #lấy thêm phần đuôi để get order
        for item in (json.loads(res.text)['orders']):
            orderId = item['name']
            #created_at = item['created_at_in_timezone']
            created_at = item['created_at']
            total_price = item['total_price']
            city = item['billing_address']['city']
            #Viết ra order thuộc website nào dựa vào link url order của site
            order_status_url = item['order_status_url']
            dotstart = item['order_status_url'].find("//")
            dotend = item['order_status_url'].rfind(".")
            shop_site = order_status_url[(dotstart+2):dotend].upper()
            #
            number_line_item = len(item['line_items'])
            #tạo thêm order vào database
            try:
                Order.objects.update_or_create(
                    orderId=orderId,
                    total_price=total_price,
                    created_at=created_at,
                    city = city,
                    shop_site= shop_site,
                    number_line_item=number_line_item
                )
            except:
                print(orderId + " existed")
            for line_item in range(number_line_item):
                order       = orderId #  item['name']
                line_item_order_id = orderId+"__"+str(line_item)
                #shop_site   = shop_site
                fulfillment_status = item['line_items'][line_item]['fulfillment_status']
                #lấy hình ảnh sản phầm tử shopify
                product_id  = item['line_items'][line_item]['product_id']
                url_get_image = site + "products/"+str(product_id)+"/images.json"
                try:
                    res1 = requests.get(url_get_image)
                    img =json.loads(res1.text)['images']
                    print (img[0]['src'])
                    image_src   = img[0]['src']
                except:
                    image_src = item['line_items'][line_item]['name']
                #created_at  = created_at]
                price       = item['line_items'][line_item]['price']
                quantity    = item['line_items'][line_item]['quantity']
                sku         = item['line_items'][line_item]['sku']
                title       = item['line_items'][line_item]['title']
                vendor      = item['line_items'][line_item]['vendor']
                #tạo thêm line item order vào database
                try:
                    Line_Item_Order.objects.get_or_create(
                    line_item_order_id=line_item_order_id,
                    order=order,
                    shop_site=shop_site,
                    created_at=created_at,
                    fulfillment_status = fulfillment_status,
                    image_src=image_src,
                    product_id = product_id,
                    price = price,
                    quantity = quantity,
                    sku = sku,
                    title = title,
                    vendor = vendor,
                )
                except:
                    print(line_item_order_id+"existed")
###################################



    allData=Line_Item_Order.objects.all().order_by("-created_at")
    allData1=Order.objects.all().order_by("-created_at")
    #context = {"orderId":orderId,"orderName":orderName,"total_price":total_price,"i":i,"number":number}
    context = {'data':allData,'data1':allData1}
    return render(request, "order/index.html", context )

def index1(request):
    res = requests.get("https://bcf351dba928d38aa14a084313104bbf:fe17f0728674c6cab25db9f6b522da2b59fb68660bf293c13596775af2927179@mysticlifee.onshopbase.com/admin/orders.json")
    for item in (json.loads(res.text)['orders']):
        print(item['order_number'])
        orderId = item['name']
        total_price = item['total_price']
        #lấy thời gian--
        # date_time_str = item['created_at']
        # date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%dT%H:%M:%S%z')
        # created_at = date_time_obj
        created_at = item['created_at_in_timezone']
        #lấy thời gian--
        Order.objects.update_or_create(orderId=orderId,total_price=total_price,created_at=created_at)
        allData=Order.objects.all().order_by("-created_at")
    context = {'data':allData}
    return render(request, "order/index1.html", context )

def index2(request):
    allData=Line_Item_Order.objects.all().order_by("-created_at")
    context = {'data':allData}
    return render(request, "order/index2.html", context )

