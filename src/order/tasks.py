from __future__ import absolute_import, unicode_literals
import logging

from django.conf import settings
from mydjango.celery import app

logger = logging.getLogger("celery")

import requests
from bs4 import BeautifulSoup
from .models import DataModel

# vao vnexpress 
# craw data 
# insert database 
# run 5 phut 1 lan


@app.task
def get_data_vnexpress():
    url = "https://vnexpress.net/the-gioi"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    for item in soup.find_all('h3'):
        print(item.text)
        DataModel.objects.get_or_create(
            title=item.text,
            link=item.a['href']
        )



@app.task
def hello():
    print(" xin chao")


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(10.0, test.s('hello'), name='add every 10')

    # Calls test('world') every 30 seconds
    sender.add_periodic_task(30.0, test.s('world'), expires=10)

    # Executes every Monday morning at 7:30 a.m.
    sender.add_periodic_task(
        crontab(hour=7, minute=30, day_of_week=1),
        test.s('Happy Mondays!'),
    )

@app.task
def test(arg):
    print(arg)

@app.task
def add(x, y):
    z = x + y
    print(z)