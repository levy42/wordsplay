from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def home(request, *args, **kwargs):
    return render(request, 'index.html')


@login_required
def test(request, *args, **kwargs):
    return render(request, 'test.html')
