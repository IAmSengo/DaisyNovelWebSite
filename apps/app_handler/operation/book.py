# -*- coding: UTF-8 -*-
# __author__ = 'Sengo'


def create_book(request):
    bk_name = request.POST["bk_name"]
    bk_author = "aaa"  # TODO fetch from session
    bk_description = request.POST["bk_description"]
    bk_level = request.POST["bk_level"]
    bk_sex = request.POST["bk_sex"]
