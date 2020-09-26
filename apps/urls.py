from django.urls import path
from apps.app_handler.operation import invitation
from apps.app_handler import views

urlpatterns = [
    path('', views.index),  # 测试用
    path('op/gen_invitation_code', invitation.gen_invitation_code),  # 生成邀请码
    path('op/redeem_invitation_code', invitation.redeem_invitation_code)  # 使用邀请码
]
