from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def yosan(request):
    return render(request, 'yosan/yosan.html', {'sales': 'c1'})
