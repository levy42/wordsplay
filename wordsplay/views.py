from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def home(request, *args, **kwargs):
    return render(request, 'index.html')


@login_required
def test(request, *args, **kwargs):
    return render(request, 'test.html')


@login_required
def user_profile(request):
    return render(request, 'users/user_profile.html')
