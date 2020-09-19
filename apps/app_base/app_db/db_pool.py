# -*- coding: UTF-8 -*-
# __author__ = 'Sengo'


import os
from contextlib import contextmanager

import psycopg2.pool
import psycopg2.extras

'''
Usage: https://github.com/python-wells/postgres-connection-pool/blob/master/test_pool.py 
Not in use
'''

POOL = None
CONF = {
    "db.poolmin": os.getenv('DBPOOLMIN', "3"),
    "db.poolmax": os.getenv('DBPOOLMAX', "10"),
    "db.host": os.getenv('PGHOST', "localhost"),
    "db.port": os.getenv('PGPORT', "5432"),
    "db.name": os.getenv('PGDATABASE', "luck"),
    "db.user": os.getenv('PGUSER', "postgres"),
    "db.password": os.getenv('PGPASSWORD', "xxxx"),
}


def _get_pool():
    global POOL
    if not POOL:
        POOL = psycopg2.pool.ThreadedConnectionPool(
            int(CONF.get("db.poolmin")),
            int(CONF.get("db.poolmax")),
            host=CONF.get("db.host"),
            port=int(CONF.get("db.port")),
            database=CONF.get("db.name"),
            user=CONF.get("db.user"),
            password=CONF.get("db.password"))
    return POOL


@contextmanager
def get_conn():
    conn = _get_pool().getconn()
    try:
        yield conn
        conn.commit()
    except:
        conn.rollback()
        raise
    finally:
        POOL.putconn(conn)


@contextmanager
def get_cursor():
    with get_conn() as conn:
        yield conn.cursor()


@contextmanager
def get_dict_cursor():
    with get_conn() as conn:
        yield conn.cursor(cursor_factory=psycopg2.extras.DictCursor)


