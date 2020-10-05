# -*- coding: UTF-8 -*-
# __author__ = 'Sengo'
"""邀请码相关"""
import random
import string

from apps.app_dao.auth_invitation_dao import is_invitation_code_exist, insert_invitation_code, fetch_invitation_by_code,\
    redeem_code
from apps.app_dao.auth_user_dao import is_user_name_exist, create_user, is_email_exist
from apps.app_handler import json_response
from apps.app_base.app_utils import days_till_now, get_client_ip
from apps.app_base.app_log import LOG

from ratelimit.decorators import ratelimit
from apps.settings import DEBUG
import traceback

INVITATION_CODE_EXPIRE_DAY = 7  # 邀请码过期天数
USER_NAME_LENGTH_LIMITATION = 8  # 用户名长度限制


def gen_invitation_code(request):
    """Generate random invitation code"""
    u_id = "123"  # TODO 从cookie里面拿uid， 扣除对应用户积分等
    try:
        code = _gen_random_string()
        while is_invitation_code_exist(code):  # 换成存数据库
            code = _gen_random_string()
        insert_invitation_code(code, u_id)
        return json_response({"invitation_code": code})
    except Exception:
        LOG.error("gen_invitation_code", traceback.format_exc(), u_id=u_id, ip=get_client_ip(request))
        return json_response(code=500)


@ratelimit(key='ip', rate='1/5m', block=not DEBUG)
def redeem_invitation_code(request):
    """使用邀请码注册, 传入邀请码，用户名，密码，邮箱"""
    user_name = request.POST["user_name"]
    password = request.POST["password"]
    email = request.POST["email"]
    invitation_code = request.POST["invitation_code"]
    try:
        if len(user_name) > USER_NAME_LENGTH_LIMITATION:
            return json_response({"msg": "用户名长度大于8个字符，一个汉字也是一个字符。"})
        # 判断用户名是否使注册过
        if is_user_name_exist(user_name):
            return json_response({"msg": "该用户名已存在！"})
        # 判断邮箱是否被注册过:
        if is_email_exist(email):
            return json_response({"msg": "该邮箱已被注册过！"})

        # Check whether the invitation_code is valid
        is_valid, msg = _is_invitation_code_valid(invitation_code)
        if not is_valid:
            return json_response({"msg": msg})

        # Create the account
        client_ip = get_client_ip(request)
        u_id = create_user(user_name, password, email, client_ip)
        if u_id:  # If create account successfully, redeem the code
            redeem_code(invitation_code, u_id)
        return json_response({"msg": "兑换邀请码成功,账号已成功注册！"})
    except Exception:
        LOG.error("gen_invitation_code", traceback.format_exc(), ip=get_client_ip(request), user_name=user_name,
                  email=email, invitation_code=invitation_code)
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
        return True, "有效的邀请码。"




