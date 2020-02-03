from __future__ import absolute_import, unicode_literals
#從celery library 輸入shared_task功能
from celery import shared_task
import time

#autodiscover_tasks() 會搜尋所有tasks.py 被標記@shared_task的功能
@shared_task
def say_hello():
    #模擬繁重的運算
    time.sleep(6)

    print('小工人啟動!你好')
    return None

@shared_task
def add(x, y):
    return x + y

@shared_task
def xsum(numbers):
    return sum(numbers)

@shared_task
def rename_widget(widget_id, name):
    w = Widget.objects.get(id=widget_id)
    w.name = name
    w.save()
