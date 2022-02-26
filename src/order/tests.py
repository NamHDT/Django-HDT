from unicodedata import name
from django.test import TestCase
import requests
import json
#from .models import Order
from rest_framework.response import Response
import datetime

from order.models import Line_Item_Order, Order
# Create your tests h$ git --versionere.

url=[]
url.append("https://bcf351dba928d38aa14a084313104bbf:fe17f0728674c6cab25db9f6b522da2b59fb68660bf293c13596775af2927179@mysticlifee.onshopbase.com/admin/orders.json")
url.append("https://ae1c566c25bbabcbbc7c5176b1be07dc:6b5642a08755a48b143c5d1743a47210fea75605b34e459acf7a82805e7fa0ce@olafize.onshopbase.com/admin/orders.json")
url.append("https://693cd44a9f7cce289e7b44e9a17c61b7:cd12c08bc8eeeee69be8db3ae67b8543081fcb24527698c1520d9e96f0418341@mysticlif-com.onshopbase.com/admin/orders.json")
for site in url:
    res = requests.get(site)
    for item in (json.loads(res.text)['orders']):
        print(item['order_number'])
        orderId = item['name']
        created_at = item['created_at_in_timezone']
        total_price = item['total_price']
        city = item['additional_information']['city']
        #Viết ra order thuộc website nào dựa vào link url hóa đơn của site (shopbase)
        invoice = item['invoice_url']
        dotstart = item['invoice_url'].find(".")
        dotend = item['invoice_url'].rfind(".")
        shop_site = invoice[(dotstart+1):dotend].upper()
        #
        number_line_item = len(item['line_items'])
        #tạo thêm order vào database
        cs=Order.objects.update_or_create(
            orderId=orderId,
            total_price=total_price,
            created_at=created_at,
            city = city,
            shop_site= shop_site,
            number_line_item=number_line_item
        )
        for line_item in range(number_line_item):
            order       = orderId #  item['name']
            line_item_order_id = orderId+"__"+str(line_item)
            #shop_site   = shop_site
            fulfillment_status = item['line_items'][line_item]['fulfillment_status']
            image_src   = item['line_items'][line_item]['image_src']
            product_id  = item['line_items'][line_item]['product_id']
            price       = item['line_items'][line_item]['price']
            quantity    = item['line_items'][line_item]['quantity']
            sku         = item['line_items'][line_item]['sku']
            title       = item['line_items'][line_item]['title']
            vendor      = item['line_items'][line_item]['vendor']
            #tạo thêm line item order vào database
            Line_Item_Order.objects.update_or_create(
            order=order,
            line_item_order_id=line_item_order_id,
            shop_site=shop_site,
            fulfillment_status = fulfillment_status,
            image_src=image_src,
            product_id = product_id,
            price = price,
            quantity = quantity,
            sku = sku,
            title = title,
            vendor = vendor,
        )

# ############ lệnh lấy order từ shopbase

# res = requests.get("https://693cd44a9f7cce289e7b44e9a17c61b7:cd12c08bc8eeeee69be8db3ae67b8543081fcb24527698c1520d9e96f0418341@mysticlif-com.onshopbase.com/admin/orders.json")

# json_data = res.text
# json_object = json.loads(json_data)
# json_formatted_str = json.dumps(json_object, indent=2)
#print(json_formatted_str)
# for item in (json.loads(res.text)['orders']):
#     test = item['line_items'][0]['fulfillment_status']
#     print (test)
#     print(item['line_items'][0]['name'])
#     number_line_item = len(item['line_items'])
#     orderId = item['name']
#     fulfillment_status = item['line_items'][0]['fulfillment_status']
#     print(fulfillment_status)
#     for line_item in range(number_line_item):
#         order       = orderId #  item['name']
#         print (order)
#         line_item_order_id = orderId+"__"+str(line_item)
#         print(line_item_order_id)
#         #shop_site   = shop_site
#         fulfillment_status = item['line_items'][line_item]['fulfillment_status']
#         print(fulfillment_status)
#     # for i in range(number_item):
    #     line_item_order_id = orderId+"__"+str(i)
    #     print(line_item_order_id)


    # orderId = item['name']
    # invoice = item['invoice_url']
    # dotstart = item['invoice_url'].find(".")
    # dotend = item['invoice_url'].rfind(".")
    # shop_site = invoice[(dotstart+1):dotend].upper()
    # print (shop_site)
#########
# ## format của date trong shopbase
    # print(item['created_at'])
    # date_time_str = item['created_at']
    # date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%dT%H:%M:%S%z')
    # print('Date:', date_time_obj.date())
    # print('Time:', date_time_obj.time())
    # print('Date-time:', date_time_obj)
# ###################################
# url=[]
# url.append("https://bcf351dba928d38aa14a084313104bbf:fe17f0728674c6cab25db9f6b522da2b59fb68660bf293c13596775af2927179@mysticlifee.onshopbase.com/admin/orders.json")
# url.append("https://ae1c566c25bbabcbbc7c5176b1be07dc:6b5642a08755a48b143c5d1743a47210fea75605b34e459acf7a82805e7fa0ce@olafize.onshopbase.com/admin/orders.json")
# for site in url:
#     print (site)
#     print (site[2:10])