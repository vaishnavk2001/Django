from django.http import HttpResponse
from django.shortcuts import render


def fun(request):
    return HttpResponse('hello world')
