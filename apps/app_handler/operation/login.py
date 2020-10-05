# -*- coding: UTF-8 -*-
# __author__ = 'Sengo'
from ratelimit.decorators import ratelimit
from apps.settings import DEBUG
from apps.app_base.app_log import LOG
from apps.app_handler import json_response
from apps.app_dao.auth_user_dao import fetch_user_info_by_email_password
import traceback

LOGIN_SESSION_EXPIRE_DAY = 1


@ratelimit(key='ip', rate='3/5m', block=not DEBUG)
def user_login(request):
    """
    :param request: 传入email和password来登入， 频率限制
    :return:
    """
    email = request.POST["email"]
    password = request.POST["password"]

    try:
        user_info = fetch_user_info_by_email_password(email, password)
        if not user_info:
            return json_response({"msg": "登录失败，邮箱或密码错误！"})
        # Create Session
        request.session[user_info['u_id']] = user_info
        request.session.set_expiry(LOGIN_SESSION_EXPIRE_DAY*24*3600)
        return json_response({"msg": "登录成功！", "user_info": user_info})
    except Exception:
        LOG.error("user_login", traceback.format_exc(), email=email, password=password)
        return json_response(code=500)