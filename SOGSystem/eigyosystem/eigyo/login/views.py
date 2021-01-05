from django.shortcuts import render, redirect
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.urls import reverse

from eigyosystem import models
from eigyosystem.eigyo.login.forms import UserForm


# def logineigyo(request):
#     if request.method == 'POST':
#
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = auth.authenticate(username=username, password=password)
#             if user is not None and user.is_active:
#                 auth.login(request, user)
#                 return HttpResponseRedirect(reverse('eigyosystem:index'))
#             else:
#                 return render(request, 'login/logineigyo.html',
#                               {'form': form, 'message': 'Wrong password Please Try agagin'})
#     else:
#         form = LoginForm()
#
#     return render(request, 'login/logineigyo.html', {'form': form})
#
#
# def test(request):
#
#     print('7777777777745564564567456456564')
#     return render(request, 'test.html', {'form': 'form'})

def logineigyo(request):
    if request.session.get('is_login', None):
        return redirect('eigyosystem:index')

    next = request.GET.get('next', '')

    if request.method == "POST":
        form = UserForm(request.POST)
        message = "请检查填写的内容！"
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                request.session['is_login'] = True
                request.session['user_id'] = user.username
                request.session['user_name'] = user.first_name + user.last_name
                if next == "":
                    return HttpResponseRedirect(reverse('eigyosystem:index'))
                    # return HttpResponseRedirect(reverse('eigyosystem:index', args=[user.id]))
                else:
                    return HttpResponseRedirect(next)
            else:
                return render(request, 'login/logineigyo.html',
                              {'form': form, 'message': 'ユーザ名またはパスワードが正しくありません。入力し直してください。'})
        return render(request, 'login/logineigyo.html', {'form': form})
    form = UserForm()
    return render(request, 'login/logineigyo.html', {'form': form})

