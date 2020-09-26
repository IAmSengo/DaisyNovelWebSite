# -*- coding: UTF-8 -*-
# __author__ = 'Sengo'

from django.http import JsonResponse


def json_response(dic=None, code=200, msg=""):
    if dic is None:
        dic = {}
    dic["code"] = code
    if msg:
        dic["msg"] = msg
    return JsonResponse(dic)




