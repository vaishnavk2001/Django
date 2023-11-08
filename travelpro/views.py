from django.http import HttpResponse
from django.shortcuts import render


# def fun(request):
#     return HttpResponse('hello world')

def fun(request):
    return render(request, 'home.html', {'name': 'vaishnav'})
