# -*- coding: UTF-8 -*-
# __author__ = 'Sengo'
from apps.app_base.app_db import db_fetch_one, db_execute
from apps.app_base.app_utils import get_cur_time


def is_invitation_code_exist(code):
    sql = "SELECT invitation_code FROM auth_invitation WHERE invitation_code = %s"
    return db_fetch_one(sql, [code])


def insert_invitation_code(code, from_user):
    cur_time = get_cur_time()
    sql = "INSERT INTO auth_invitation(invitation_code, from_user, create_date) VALUES (%s, %s, %s)"
    return db_execute(sql, [code, from_user, cur_time])


def fetch_invitation_by_code(code):
    sql = "SELECT * FROM auth_invitation WHERE invitation_code = %s"
    return db_fetch_one(sql, [code])


def redeem_code(code, u_id):
    sql = "UPDATE auth_invitation SET to_user = %s WHERE invitation_code = %s"
    return db_execute(sql, [u_id, code])
