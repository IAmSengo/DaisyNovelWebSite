# -*- coding: UTF-8 -*-
# __author__ = 'Sengo'
from django.db import connection


def db_execute(sql, params=None):
    """
    Base execute sql
    :param sql: Sql command
    :param params: Dict type or list type
    """
    with connection.cursor() as cursor:
        cursor.execute(sql, params)
    return True


def db_fetch_one(sql, params=None):
    """Return one row from a cursor as dict"""
    with connection.cursor() as cursor:
        cursor.execute(sql, params)
        desc = cursor.description
        data = cursor.fetchone()
        row = dict(zip([col[0] for col in desc], data)) if data else None
    return row


def db_fetch_all(sql, params=None):
    """Return all row from a cursor as a list of dict"""
    with connection.cursor() as cursor:
        cursor.execute(sql, params)
        desc = cursor.description
        object_list = [
            dict(zip([col[0] for col in desc], row))
            for row in cursor.fetchall()
        ]
        cursor.close()
    return object_list


def db_insert_lastrowid(sql, params=None):
    """Insert and return last row id by using returning
    e.g. INSERT INTO test (name) VALUES (%(name)s) RETURNING id"
    """
    with connection.cursor() as cursor:
        cursor.execute(sql, params)
        row_id = cursor.fetchone()[0]
    return row_id


