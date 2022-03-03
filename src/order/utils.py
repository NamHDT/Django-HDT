import requests
import json
from .models import Order

def save_email(email, address):
    Order.objects.create(email=email, address=address)
    obj, created = Order.objects.get_or_create(
        email=email, address=address
    )

def reward_for_city():

    r = requests.get("https://bcf351dba928d38aa14a084313104bbf:fe17f0728674c6cab25db9f6b522da2b59fb68660bf293c13596775af2927179@mysticlifee.onshopbase.com/admin/orders.json")
    data = json.loads(r.text)
    citys = []
    for item in data['orders']:
        ct = item['additional_information']['city']
        save_email(email=item['email'], address=ct)
        citys.append(ct)
    return citys