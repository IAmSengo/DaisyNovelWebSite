# -*- coding: UTF-8 -*-
# __author__ = 'Sengo'
from apps.app_base.app_db import db_fetch_one, db_insert_lastrowid
from apps.app_base.app_utils import get_cur_time
import hashlib
from django.contrib.auth.hashers import make_password

PASSWORD_SALT = "Daisy"


def is_user_name_exist(user_name):
    sql = "SELECT u_id FROM auth_user WHERE user_name = %s"
    return db_fetch_one(sql, [user_name])


def is_email_exist(email):
    sql = "SELECT u_id FROM auth_user WHERE email = %s"
    return db_fetch_one(sql, [email])


def create_user(user_name, password, email, reg_ip):
    cur_time = get_cur_time()
    password = make_password(password, salt=PASSWORD_SALT, hasher='pbkdf2_sha1')
    sql = "INSERT INTO auth_user (user_name, password, email, reg_ip, date_join, last_login) " \
          "VALUES (%s, %s, %s, %s, %s, %s) RETURNING u_id"
    return db_insert_lastrowid(sql, [user_name, password, email, reg_ip, cur_time, cur_time])


def fetch_user_info_by_email_password(email, password):
    password = make_password(password, salt=PASSWORD_SALT, hasher='pbkdf2_sha1')
    sql = "SELECT u_id, user_name, level, coin, fans, is_blocked, email FROM auth_user " \
          "WHERE email = %s AND password = %s"
    return db_fetch_one(sql, [email, password])


if __name__ == '__main__':
    print(hashlib.md5("ass".encode()).hexdigest())
