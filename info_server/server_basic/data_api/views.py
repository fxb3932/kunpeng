from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt    #可post调用url
import json

import requests
# Create your views here.
import main
def index(request):
    print('start index data_api')

    # 权限检查
    auth_data = {
        'request': request
        , 'net': False
        , 'login': False
        , 'perm': ''
    }
    resp_auth = main.auth(auth_data)
    if resp_auth.get('code') == False:
        return render(request, 'alarm/resp.html', {"message": resp_auth.get('msg')})


    resp_info = {
        'title': 'data_api'
    }
    # print(req)
    return render(request, 'data_api/index.html', resp_info)

from .models import api
@csrf_exempt
def api_menu(request):
    print('start api_menu')
    # print(api.objects.all())

    api_list = []
    for line in api.objects.all():
        api_list.append({
            "id": line.api_id
            , "url": 'http://' + request.META.get('HTTP_HOST') + '/' + line.url
            , "text": line.text
            , "par": line.par
            , "dev_oper": line.dev_oper
        })

    resp = {
        "code": 0
        , "msg": ''
        , "data": api_list
    }
    return HttpResponse(json.dumps(resp), content_type="application/json")


@csrf_exempt
def api_run(request):
    print('start api_run')

    # API调用示例
    # res = requests.post(
    #     url='http://' + request.META.get('HTTP_HOST') + '/' + 'data_api/oper/'
    #     , data='{}'
    # )
    # resp = json.loads(res.text)
    # print(resp)

    post_data = json.loads(request.POST.get('data'))
    url = post_data.get('url')
    data = post_data.get('par')
    res = requests.post(url=url, data=data)

    resp = json.loads(res.text)
    return HttpResponse(json.dumps(resp), content_type="application/json")


import sys
sys.path.append('apis')

# from .apis.__init__ import *
import glob
# import apis
from cmdb.models import *
def api_call(request, api):
    print('test')




    data = '111'
    return HttpResponse(json.dumps(data), content_type="application/json")




