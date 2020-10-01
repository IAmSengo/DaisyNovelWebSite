# -*- coding: UTF-8 -*-
# __author__ = 'Sengo'
import logging


def _format_msg(name, content, log_level, **kwargs):
    msg = 'FUNCTION:%s 【%s】>> {%s}' % (str(name), log_level, str(content))
    for key, values in kwargs.items():
        msg += " | %s: {%s}" % (str(key), str(values))
    return msg


class Logger(object):
    def __init__(self):
        self.log = logging.getLogger(__name__)

    def error(self, func_name, content, **kwargs):
        self.log.error(_format_msg(func_name, content, "ERROR", **kwargs))

    def info(self, func_name, content, **kwargs):
        self.log.info(_format_msg(func_name, content, "INFO", **kwargs))

    def warn(self, func_name, content, **kwargs):
        self.log.warning(_format_msg(func_name, content, "WARN", **kwargs))