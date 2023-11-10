from django.http import HttpResponse
from django.shortcuts import render


# def fun(request):
#     return HttpResponse('hello world')

def fun(request):
    return render(request, 'home.html', {'name': 'vaishnav'})


def addition(request):
    n_num1 = int(request.GET['num1'])
    n_num2 = int(request.GET['num2'])
    num3 = n_num1 + n_num2
    return render(request, 'result.html',{'value':num3})
