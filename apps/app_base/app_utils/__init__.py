# -*- coding: UTF-8 -*-
# __author__ = 'Sengo'
import time


def get_cur_time():
    """获取系统当前时间，精确到毫秒，13位数字字符串"""
    return str(int(time.time() * 1000))


def convert_time_to_date(string_digit_time):
    """将 13位数字字符串时间 转为 日期格式"""
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(float(string_digit_time) / 1000))


def days_till_now(string_digit_time):
    """给一个13位字符串过去的时间，返回这个时间距离当前多少天"""
    seconds = (int(get_cur_time()) - int(string_digit_time)) // 1000
    return seconds // (3600 * 24)


def merge_dics(*args):
    """传入多个map， 合并为1个"""
    d1 = {}
    for d in args:
        d1.update(d)
    return d1


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

if __name__ == '__main__':
    t = get_cur_time()
    print(t)
    print(convert_time_to_date(t))
    print(days_till_now(1501003670669))