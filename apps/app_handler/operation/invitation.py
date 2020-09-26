# -*- coding: UTF-8 -*-
# __author__ = 'Sengo'
"""邀请码相关"""
import random
import string

from apps.app_dao.invitation_dao import is_invitation_code_exist, insert_invitation_code, fetch_invitation_by_code,\
    redeem_code
from apps.app_handler import json_response
from apps.app_base.app_utils import days_till_now


INVITATION_CODE_EXPIRE_DAY = 3  # 邀请码过期天数


def gen_invitation_code(request):
    """Generate random invitation code"""
    try:
        u_id = "123"  # TODO 从cookie里面拿uid， 扣除对应用户积分等
        code = _gen_random_string()
        while is_invitation_code_exist(code):  # 换成存数据库
            code = _gen_random_string()
        insert_invitation_code(code, u_id)
        return json_response({"invitation_code": code})
    except Exception as e:
        return json_response(code=500)


def redeem_invitation_code(request):
    """使用邀请码"""
    try:
        u_id = "543"  # TODO 从cookie里面拿uid
        code = request.POST["invitation_code"]

        # Check whether the code is valid
        is_valid, msg = _is_invitation_code_valid(code)
        if not is_valid:
            return json_response({"msg": msg}, code=400)

        # Redeem the code for this user
        redeem_code(code, u_id)
        return json_response({"msg": "兑换邀请码成功！"})

    except Exception as e:
        return json_response(code=500)


def _gen_random_string(length=15):
    char_pool = string.ascii_letters + string.digits
    return ''.join([random.choice(char_pool) for _ in range(length)]) + "Daisy"


def _is_invitation_code_valid(code):
    """
    Check if the code is exist, used and expired
    Return: Bool, String Msg
    """
    row = fetch_invitation_by_code(code)
    if not row:
        return False, "兑换邀请码失败，该邀请码不存在！"
    elif row.get("to_user"):
        return False, "兑换邀请码失败，该邀请码已被使用。"
    elif days_till_now(row["create_date"]) > INVITATION_CODE_EXPIRE_DAY:
        return False, "兑换邀请码失败，该邀请码已过期。"
    else:
        return True, ""






if __name__ == '__main__':

    print(_gen_random_string(15))
