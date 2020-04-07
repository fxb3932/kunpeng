
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.http import HttpResponse, Http404



# Create your views here.
def index(request):
    req = {}
    test = 'aaa'
    print(test)
    return render(request, 'monitor/index.html', req)