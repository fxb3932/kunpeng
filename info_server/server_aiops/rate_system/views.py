from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt  # 可post调用url
import sys
import json
import os



# Create your views here.

import main
import requests
def index(request):
    print('start index rota_day')
    search_type=request.GET.get('type')

    bank_info_list = []
    if search_type == "get":
        search_type = "get"
    elif search_type == "search":
        search_type = "search"

        # 调用数据中台API
        res = requests.post(
            url='http://' + request.META.get('HTTP_HOST') + '/' + 'data_api/cmdb_info/'
            , data={'comm_i_info_stat': 0}
        )
        resp = json.loads(res.text)

        for line in resp.get('comm_i_c_config_bank'):
            # yhdm=line.get('yhdm')
            # name=line.get('name')
            # name_ch=line.get('name_ch')
            # bank_msg=str(yhdm)+'_'+str(name)+'_'+str(name_ch)
            bank_info_list.append(line)


    else:
        search_type ="get"

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

    req = {
        'title': '系统成功率'
        ,'search_type':search_type
        ,'bank_info_list':bank_info_list

    }
    # print(req)
    return render(request, 'rate_system/index.html', req)
def indextmp(request):
    print('start index rota_day')
    search_type=request.GET.get('type')
    bank_info_list = []
    if search_type == "get":
        search_type = "get"
    elif search_type == "search":
        search_type = "search"

        # 调用数据中台API
        res = requests.post(
            url='http://' + request.META.get('HTTP_HOST') + '/' + 'data_api/cmdb_info/'
            , data={'comm_i_info_stat': 0}
        )
        resp = json.loads(res.text)

        for line in resp.get('comm_i_c_config_bank'):
            # yhdm=line.get('yhdm')
            # name=line.get('name')
            # name_ch=line.get('name_ch')
            # bank_msg=str(yhdm)+'_'+str(name)+'_'+str(name_ch)
            bank_info_list.append(line)


    else:
        search_type ="get"

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

    req = {
        'title': '系统成功率'
        ,'search_type':search_type
        ,'bank_info_list':bank_info_list

    }
    # print(req)
    return render(request, 'rate_system/indextmp.html', req)

@csrf_exempt
def getData_rateSystem(request):
    print('index get_table_data')

    input_data = request.POST.get('input_data')

    sInputDate=input_data.split('-')[0]+input_data.split('-')[1]+input_data.split('-')[2]
    trans_info = []
    filename = "/home/insp_ap/inspect/rate_system/"+"rate_system."+sInputDate
    if os.path.exists(filename)  == False:
        resp={
        'title': 'rate_system12312'
        , 'trans_info': [{'date':'无数据'}]
        }
        return HttpResponse(json.dumps(resp), content_type="application/json")

    sum_trans_tot=0
    sum_timeouterr_num=0
    sum_sqlerr_num=0
    sum_sys_rate=0
    tran_date=0

    with open(filename, 'r', encoding='GBK') as f:
        for line in f.readlines():
            bank_ch_name = line.split('|')[1]
            bank_name = line.split('|')[2]
            bank_no = line.split('|')[3]
            trans_tot = line.split('|')[4]
            timeouterr_num = line.split('|')[5]
            sqlerr_num = line.split('|')[6].split('\n')[0].split(' ')[0]

            #合成总体交易
            sum_trans_tot += int(trans_tot)
            sum_timeouterr_num += int(timeouterr_num)
            sum_sqlerr_num += int(sqlerr_num)
            try:
                sys_rate = round((int(trans_tot) -int(timeouterr_num) - int(sqlerr_num)) / int(trans_tot) * 100,5)
                print(bank_ch_name+":"+str(sys_rate))
            except:
                sys_rate=0
            dict_trans = {
                'date':input_data
                ,'bank_ch_name': bank_ch_name
                , 'bank_name': bank_name
                , 'bank_no': bank_no
                , 'trans_tot': trans_tot
                , 'timeouterr_num': timeouterr_num
                , 'sqlerr_num': sqlerr_num
                , 'sys_rate': sys_rate
            }
            trans_info.append(dict_trans)
            tran_date=input_data

    sum_sys_rate = round((int(sum_trans_tot) -int(sum_timeouterr_num) - int(sum_sqlerr_num)) / int(sum_trans_tot) * 100,5)
    sum_trans_info=[
        {
            'date':tran_date
            ,'sum_trans_tot':sum_trans_tot
            ,'bank_name':'所有行'
            ,'sum_timeouterr_num':sum_timeouterr_num
            ,'sum_sqlerr_num':sum_sqlerr_num
            ,'sys_rate':sum_sys_rate
        }
    ]

    resp= {
        'title': 'rate_system12312'
        , 'trans_info': trans_info
        , 'sum_trans_info':sum_trans_info
    }
    print(resp)
    return HttpResponse(json.dumps(resp), content_type="application/json")

from main import Shell
@csrf_exempt
def getData_rateSystemRange(request):
    print('index get_table_data')

    input_data = json.loads(request.POST.get('input_data'))

    date_select = input_data.get('date_select') #2020-03-16 -2020-03-18
    bank_select = input_data.get('bank_select')


    data_begin=date_select.split(' - ')[0].replace('-','')
    data_end=date_select.split(' - ')[1].replace('-','')
    check_bank_no=bank_select
    shell=Shell()
    shell_name="sh /home/insp_ap/inspect/src/rate_system/analyze_system_err.sh"+' '+check_bank_no+' '+data_begin+' '+data_end
    resp=shell.runCmd(shell_name)


    list_len=len(resp[1].decode('gbk').strip())

    if list_len < 1 :
        trans_info = [{'date': '无数据','sys_rate':100}]
        print("无数据直接返回")
        resp = {
            'title': '系统成功率'
            , 'trans_info': trans_info
        }
        return HttpResponse(json.dumps(resp), content_type="application/json")


    trans_info=[]
    for line in resp[1].decode('gbk').strip().replace('\r', '').split('\n'):
        print(line)
        input_data = line.split('|')[0]
        bank_ch_name = line.split('|')[1]
        bank_name = line.split('|')[2]
        bank_no = line.split('|')[3]
        trans_tot = line.split('|')[4]
        timeouterr_num = line.split('|')[5]
        sqlerr_num = line.split('|')[6].split('\n')[0]
        try:
            sys_rate = round((int(trans_tot) -int(timeouterr_num) - int(sqlerr_num)) / int(trans_tot) * 100,2)
        except:
            sys_rate=0
        dict_trans = {
            'date':input_data
            ,'bank_ch_name': bank_ch_name
            , 'bank_name': bank_name
            , 'bank_no': bank_no
            , 'trans_tot': trans_tot
            , 'timeouterr_num': timeouterr_num
            , 'sqlerr_num': sqlerr_num
            , 'sys_rate': sys_rate
        }
        trans_info.append(dict_trans)
        print(trans_info)

    resp= {
        'title': '系统成功率'
        , 'trans_info': trans_info
    }
    print(resp)

    return HttpResponse(json.dumps(resp), content_type="application/json")


from cmdb.models import *
from django.db.models import Q
import configparser
import re
@csrf_exempt
def getData_ErrorDetail(request):
    print('index get_table_data')

    input_data = json.loads(request.POST.get('input_data'))

    checkDate=input_data.get('date').replace('-','')
    bank_no=input_data.get('bank_no')
    cib_file="/home/insp_ap/inspect/src/switch/nzjs/show.ini"

    with open(cib_file, 'r', encoding='GBK') as f:
        for line in f.readlines():
            if line.split(":")[6] == bank_no:
                sIp=line.split(":")[4]
                sPort=line.split(":")[8]
                break

    print(sIp + "  "+sPort)
    shell=Shell()
    resp =   shell.getKey('check[rate_system/get_errmsg.sh:'+checkDate+':'+bank_no+']',sIp,sPort)
    result = resp[1].decode('gbk').strip().replace('\n','<br>')
    print(type(result))



    resp= {
        'title': '系统成功率'
        , 'trans_info': result
    }
    print(resp)


    bb="ccc"

    return HttpResponse(json.dumps(resp), content_type="application/json")