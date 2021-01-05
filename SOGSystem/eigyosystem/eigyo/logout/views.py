from django.shortcuts import redirect
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.urls import reverse

from eigyosystem import models
from eigyosystem.eigyo.login.forms import UserForm


def logouteigyo(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("eigyosystem:logineigyo")
    request.session.flush()
    # 或者使用下面的方法
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect("eigyosystem:logineigyo")
