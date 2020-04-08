from django.shortcuts import render, redirect
from django.shortcuts import render
from django.http import HttpResponse, Http404

import json
import time

# 引入调用main函数
import os

os.sys.path.append("../")
import main

shell = main.Shell()
#导入cmdb的config
from cmdb.models import config



# Create your views here.

def index(request):
    s_date = time.strftime('%Y-%m-%d', time.localtime())
    context = {
        'yhtitle': '核心V2批处理检查',
        'yhdate': s_date,
        # 'yhtypelist':['测试1','测试2']
        'yhtypelist': ['V2核心检查']
    }
    print(context)

    return render(request, 'chkpcl_V2/index.html', context)


def demo(request):
    s_date = time.strftime('%Y-%m-%d', time.localtime())
    context = {
        'yhtitle': '核心V2批处理检查',
        'yhdate': '2019-11-27',
        # 'yhtypelist':['测试1','测试2']
        'yhtypelist': ['V2核心检查']
    }
    print(context)

    return render(request, 'chkpcl_V2/demo.html', context)


def yh_echart_demo(request):
    s_date = time.strftime('%Y-%m-%d', time.localtime())
    context = {
        'title': '核心V2批处理检查',
        'date': '2019-11-26',
        'type': ['测试1', '测试2']
    }
    print(context)
    return render(request, 'chkpcl_V2/yh_echart_demo.html', context)


from django.views.decorators.csrf import csrf_exempt  # 可post调用url


@csrf_exempt
def post_V2pcl(request):
    data_get = request.POST;


    print('----------------------------')
    check_date=data_get.get('date').replace('-','')
    print(check_date)
    check_type=data_get.get('type')
    print('----------------------------')

    # print(msg)
    dict = {
        'bank_name': "10001"
        , 'bank_chname': "杜甫"
        , 'check_status': "xianxin@layui.com"
        , 'jgnum_num': "1234"
        , "gy_num": "浙江杭州"
        , "xy_result": "点击此处，显示更多123。"
        , "pcl_result": "116"
        , "bank_no": "192.168.0.8"
    }

    plat_msg=config.objects.all().filter(plat_id="cib",plat_name='V2核心系统')
    return_list=[]
    for msg in plat_msg:
        bank_name=msg.name
        bank_chname=msg.name_ch
        bank_ip=msg.ip
        bank_port=msg.port
        bank_id=msg.team
        if bank_name[-3:] != 'CLJ':
            resp=shell.getKey("check[./chkpcl_V2/chkpclV2.sh:"+check_date+"]",bank_ip,bank_port)
            info = resp[1].decode('GBK').split('\n')
            for line_info in info:
                if line_info != "" :
                    if line_info.startswith('RETURN:') == True:
                        jg_status=line_info.lstrip('RETURN:').split("|")[0]
                        gy_status = line_info.lstrip('RETURN:').split("|")[1]
                        xd_status = line_info.lstrip('RETURN:').split("|")[2]
                        pcl_status = line_info.lstrip('RETURN:').split("|")[3]
                        if xd_status == "DEF":
                            xd_status="未开始"
                        elif xd_status == "OK":
                            xd_status = "已完成"
                        if pcl_status == "DEF":
                            pcl_status = "未开始"
                        elif pcl_status == "IN":
                            pcl_status = "进行中"
                        elif pcl_status == "OK":
                            pcl_status = "已完成"
                        print(bank_chname,jg_status,gy_status,xd_status,pcl_status)
                        check_status="OK"
                    else:
                        check_status=line_info
                    mydict = {
                        'bank_name': bank_name
                        , 'bank_chname': bank_chname
                        , 'check_status': check_status
                        , 'jgnum_num': jg_status
                        , "gy_num": gy_status
                        , "xd_result": xd_status
                        , "pcl_result": pcl_status
                        , "bank_no": bank_id
                    }
                    return_list.append(mydict)

        # print(info)

    dict_resp={
        'name':'核心V2批处理检查',
        'return_list':return_list
    }


    resp_dict = json.dumps(dict_resp)
    # print(dict)
    return HttpResponse(resp_dict, content_type="application/json")
