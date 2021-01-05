from django import forms
from django.contrib.auth.models import User
import re


# def email_check(email):
#     pattern = re.compile(r"\"?([-a-zA-Z0-9.'?{}]+@\w+\.\w+)\"?")
#     return re.match(pattern, email)


# class LoginForm(forms.Form):
#     username = forms.CharField(label='Username', max_length=50)
#     password = forms.CharField(label='Password', widget=forms.PasswordInput)
#
#     # use clean methods to define custom validation rules
#
#     def clean_username(self):
#         username = self.cleaned_data.get('username')
#         if email_check(username):
#             filter_result = User.objects.filter(email__exact=username)
#             if not filter_result:
#                 raise forms.ValidationError('This email does not exist')
#         else:
#             filter_result = User.objects.filter(username__exact=username)
#             if not filter_result:
#                 raise forms.ValidationError('This username does not exist Please register first')
#
#         return username

class UserForm(forms.Form):
    username = forms.CharField(label="ユーザー名:", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="パスワード:", max_length=256,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))
