from django.shortcuts import render

# Create your views here.

def index(request):
    print('start index trans_yh')
    req = {
        'title': 'asdf',
        'name': 'asdfsdf'
    }
    return render(request, 'trans_yh/index.html', req)

def stu(request):
    print('start index trans_yh')
    req = {
        'title': 'asdf',
        'name': 'asdfsdf'
    }
    return render(request, 'trans_yh/stu.html', req)

import cx_Oracle
def ora(request):
    print('start index trans_yh')
    req = {
        'title': 'asdf',
        'name': 'asdfsdf'
    }

    return render(request, 'trans_yh/stu.html', req)

