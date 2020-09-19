# -*- coding: UTF-8 -*-
# __author__ = 'Sengo'
from django.http import JsonResponse
from apps.app_base.app_db import *
from apps.app_base.app_redis import *


def index(request):
    output = {'foo': 'bar'}

    redis_set_map("test", output)
    print(redis_get("year"))
    return JsonResponse(redis_get("test"))