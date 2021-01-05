from django import forms


class UriageSearchForm(forms.Form):
    datestart = forms.DateField(label='期間入力', required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    dateend = forms.DateField(label='期間入力', required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    userid = forms.CharField(label="担当者コード:", required=False, max_length=2, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(label="担当者:", required=False, max_length=128,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))
    companyid = forms.CharField(label="顧客コード:", required=False, max_length=4,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    companyname = forms.CharField(label="顧客名:", required=False, max_length=128,
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))
