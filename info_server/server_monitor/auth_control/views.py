from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt    #可post调用url
import json

# Create your views here.
import main
def index(request):
    print('start index auth_control')
    # 权限检查
    auth_data = {
        'request': request
        , 'net': False
        , 'login': False
        , 'perm': 'make'
    }
    resp_auth = main.auth(auth_data)
    if resp_auth.get('code') == False:
        return render(request, 'alarm/resp.html', {"message": resp_auth.get('msg')})
    req = {
        'title': 'auth_control'
    }
    # print(req)
    return render(request, 'auth_control/index.html', req)