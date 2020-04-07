from django.shortcuts import render
from django.http import HttpResponse
from cmdb.models import config

import time
import sys
import main

# 白云德信
shell = main.Shell()

def index(request):

    print('start index topfe_reportform')
    user = request.user
    print(user)

    # if main.auth_net(request) != True:
    #     return render(request, 'alarm/resp.html', {"message": "该功能需要在生产终端上才可以访问哟：）"})
    print(user.is_authenticated)

    print(user.has_perm('myApp'))
    s_date = time.strftime('%Y-%m-%d', time.localtime())

    bank_list = []
    data = config.objects.all()
    for line in data:
        if line.user == 'topfe':
            bank_list.append({'bank_name': line.name_ch })
            #print(bank_list)
    req = {
        'title': '金卡前置月交易信息',
        'date': s_date,
        'req': bank_list,
    }
    return render(request, 'topfe_reportform/index.html', req)

import json
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def post(request):
    print('start post')
    print(request.POST)  # form 包含提交的数据
    print(request.POST.get('bank_id'))
    ip = '163.6.59.16'
    port='10071'
    #print(request.POST.get('bank_port'))
    # ip =  ''
    # port = ''
    # data = config.objects.all()
    # for line in data:
    #     if line.user == 'topfe':
    #         if line.name_ch == request.POST.get('bank_id'):
    #             ip = line.ip
    #             port = line.port

    print (ip + " | "+ port)
    #resp = shell.getKey( 'check[run_command:user:./sjtq/static.sh:' + request.POST.get('bank_id')  , ip , port)

    resp = shell.getKey('check[run_command:user:./sjtq/static.sh:]' , ip , port)
    try:
        info = resp[1].decode('GBK').split('\n')
    except:
        info = resp[1]
    print("0000000 ")
    print (info)

    list_data = []
    n = 1
    if  info != '':
        for line_info in info:
            print(line_info)
            print("line_info " + line_info.split(' ')[0])
            if line_info.split(' ')[0] != 'user':
                if line_info != '':
                    dict_data = {
                        "inst_date": line_info.split('|')[0]
                        , "trans_code": line_info.split('|')[1]
                    }
                    list_data.append(dict_data)
                    n += 1

    resp = {
        "code": 0,
        "msg": ",",
        "count": n,
        "data": list_data
    }
    return HttpResponse(json.dumps(resp), content_type="application/json")