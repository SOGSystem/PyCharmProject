from datetime import datetime
import time

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from eigyosystem.common.uriage import uriagesql
from eigyosystem.eigyo.uriage import viewcommon
from eigyosystem.eigyo.uriage.forms import UriageSearchForm


@login_required
def uriage(request):
    indexes = viewcommon.indexview()

    return render(request, 'uriage/uriage.html', {'indexes': indexes})


@login_required
def uriage_search(request):
    indexes = viewcommon.indexview()

    if request.method == "POST":
        form = UriageSearchForm(request.POST)
        if form.is_valid():
            dataresult = uriagesql(form)
            print('11111111111111111111122222222222222222222222222222222222222222222222')
            return render(request, 'uriage/uriage_jisseki.html', {'form': form, 'dataresult': dataresult})
            # return HttpResponseRedirect(reverse('eigyosystem:uriage_jisseki'), {'dataresult': dataresult})
        return render(request, 'uriage/uriage_search.html', {'form': form, 'indexes': indexes})
    form = UriageSearchForm()
    return render(request, 'uriage/uriage_search.html', {'form': form, 'indexes': indexes})


@login_required
def uriage_jisseki(request):
    indexes = viewcommon.indexview()

    return render(request, 'login/logineigyo.html', {'indexes': indexes})

