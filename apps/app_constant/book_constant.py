# -*- coding: UTF-8 -*-
# __author__ = 'Sengo'
from enum import Enum


class BookCategory(Enum):  # 小说类型
    ORIGINAL = 1  # 原创小说
    FANDOM = 2  # 同人小说


class BookProgress(Enum):  # 连载进度
    UNFINISHED = 0
    FINISHED = 1
    SUSPEND = 2


class BookLevel(Enum):  # 文章分级
    POPULAR = 1
    TEENS = 2
    LIMITED = 3
    ADULT = 4


class Sexuality(Enum):  # 文章性向
    FF = 1
    FM = 2
    GEN = 3
    MM = 4
    Multi = 5
    Other = 6


if __name__ == '__main__':
    print(Sexuality._value2member_map_)
    print(Sexuality.FF.value)


