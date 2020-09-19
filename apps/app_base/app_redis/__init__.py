# -*- coding: UTF-8 -*-
# __author__ = 'Sengo'
from django_redis import get_redis_connection
from apps.app_base.app_utils.data_encoder import JSONDataEncoder


def redis_set(key, value, timeout=None):
    """timeout=0 立即过期, timeout=None 永不超时"""
    conn = get_redis_connection('default')
    conn.set(key, value, timeout)


def redis_get(key):
    """get一个key，可以拿到对应的值或者map"""
    conn = get_redis_connection('default')
    v = conn.get(key)
    return JSONDataEncoder.decode(v)


def redis_set_map(key, value, timeout=None):
    """存入一个map到redis"""
    value = JSONDataEncoder.encode(value)
    conn = get_redis_connection('default')
    conn.set(key, value, timeout)


def redis_persist(key):
    """让一个值永不过期"""
    conn = get_redis_connection('default')
    conn.persist(key)


def redis_expire(key, timeout=None):
    """让一个值多久过期"""
    conn = get_redis_connection('default')
    conn.expire(key, timeout)


def redis_iter_keys(pattern):
    """可以用*模糊匹配， 返回一个generate"""
    conn = get_redis_connection('default')
    return conn.iter_keys(pattern)


def redis_del_pattern(pattern):
    """删除key, 但是可以用*匹配来大量删除"""
    conn = get_redis_connection('default')
    conn.delete_pattern(pattern)

