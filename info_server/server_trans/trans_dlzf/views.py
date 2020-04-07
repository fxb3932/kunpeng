from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import time

import sys
#sys.path.append('../')
import main

shell = main.Shell()
_ip = '163.51.1.10'
_port = '10066'
def index(request):
    print('start index trans_dlzf')
    user = request.user
    print(user)

    # 权限检查
    auth_data = {
        'request': request
        , 'net': True
        , 'login': False
        , 'perm': ''
    }
    resp_auth = main.auth(auth_data)
    if resp_auth.get('code') == False:
        return render(request, 'alarm/resp.html', {"message": resp_auth.get('msg')})

    print(user.has_perm('myApp'))
    s_date = time.strftime('%Y-%m-%d', time.localtime())
    # input = 'topfe_server'
    # f = open('/home/insp_ap/inspect/src/switch/' + input + '/config.ini', 'r', encoding='gbk')
    list_req = []
    resp = shell.getKey('check[run_command:user:./trans_search/get_bank_info.sh]', _ip, _port)
    try:
        info = resp[1].decode('GBK').split('\n')
    except:
        info = resp[1]

    for line_info in info:
        if line_info.startswith('RETURN:') == True:
            list_req.append({'bank_id': line_info.split(':')[1].strip()})


    # for line in f.readlines():
    #     line = line.rstrip('\n')
    #     if line.startswith('#') != True:
    #         # print(line.split(':')[1] + '_' + line.split(':')[0])
    #         list_req.append({'bank_id': line.split(':')[1], 'bank_name': line.split(':')[0]})
    # print(list_req)
    req = {
        'title': '代理支付交易查询',
        'date': s_date,
        'req': list_req
    }
    # print(req)
    return render(request, 'trans_dlzf/index.html', req)

import json
from django.views.decorators.csrf import csrf_exempt    #可post调用url
# 一级交易查询---本地查询
@csrf_exempt
def post(request):
    print('start post')
    print(request.POST)  # form 包含提交的数据
    print(request.POST.get('date'))
    print(request.POST.get('bank_id'))
    print(request.POST.get('zfskrzh'))
    print(request.POST.get('jyje'))

    resp = shell.getKey('check[run_command:user:./trans_search/get_trans_info.sh:' +
                        request.POST.get('date') +
                        '@' + request.POST.get('bank_id').strip() +
                        '@' + request.POST.get('zfskrzh') +
                        '@' + request.POST.get('jyje') +
                        '@' + request.POST.get('acct_type') +
                        ']', _ip, _port)
    try:
        info = resp[1].decode('GBK').split('\n')
    except:
        info = resp[1]

    # print(info)
    list_data = []
    n = 1
    for line_info in info:
        if line_info != '':
            # print(line_info)
            dict_data = {
                "jgdh": line_info.split('|')[0]
                , "jygy": line_info.split('|')[1]
                , "hcgy": line_info.split('|')[2]
                , "jzgylsh": line_info.split('|')[3]
                , "hcgylsh": line_info.split('|')[4]
                , "zfjylsh": line_info.split('|')[5]
                , "bdclzt": line_info.split('|')[6]
                , "dict_info": line_info.split('|')[7]
                , "ylxz": line_info.split('|')[8]
                , "jyje": line_info.split('|')[9]
                , "zfskrzh": line_info.split('|')[10]
            }
            list_data.append(dict_data)
            n+=1

    # b.jgdh, a.jygy, a.hcgy, a.jzgylsh, a.hcgylsh, b.zfjylsh, a.bdclzt,
    # (select d.dict_info from gapsdb30:t_dict d where d.dict_key=a.bdclm and d.dict_kind='dlde_bwzt'),
    # b.ylxz, b.jyje
    # print(list_data)
    resp = {
        "code": 0,
        "msg": ",",
        "count": n,
        "data": list_data
    }
    return HttpResponse(json.dumps(resp), content_type="application/json")

# 二级交易查询---联动查询
@csrf_exempt
def postTrans(request):
    print('start post')
    print(request.POST)  # form 包含提交的数据
    print(request.POST.get('date'))
    print(request.POST.get('bank_id'))
    print(request.POST.get('acct_no'))
    # time.sleep(2)
    resp = {"id": 1, "username": request.POST.get('bank_id'), "lname": "Doe", "email": "jdoe@gmail.com",
            "sdate": "4/3/2012"}
    resp = {"INFO": "二级交易查询正在施工中，暂未开放，敬请期待：）"}
    return HttpResponse(json.dumps(request.POST), content_type="application/json")
