# -*- coding: UTF-8 -*-
# __author__ = 'Sengo'
from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from apps.app_base.app_redis import *
from apps.app_handler.operation.invitation import gen_invitation_code


@cache_page(60 * 15)
def index(request):
    output = {'foo': 'bar'}
    return JsonResponse(output)