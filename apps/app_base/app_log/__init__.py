# -*- coding: UTF-8 -*-
# __author__ = 'Sengo'

from apps.app_base.app_log.logger import Logger


LOG = Logger()

if __name__ == '__main__':
    try:
        1/0
    except Exception as e:
        LOG.error("test_func", e, user="abc", ip="aaa")



