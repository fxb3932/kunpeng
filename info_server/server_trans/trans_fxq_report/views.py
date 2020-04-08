from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import time
import threading

import sys
sys.path.append('../')
import main


import datetime
from dateutil.relativedelta import relativedelta

shell = main.Shell()
swinit = main.Public()
# _ip = '163.51.1.10'
# _port = '10066'
def index(request):
    print('start index')
    print(datetime.date.today())
    print(datetime.date.today() - relativedelta(months=+1))
    print(datetime.date.today() - relativedelta(months=-3))
    start_date = str(datetime.date.today() - relativedelta(months=+1))[:-2] + '01'

    end_date = time.strftime('%Y-%m-01', time.localtime())
    list_req = [{'bank_id': 'aml_server', 'bank_name': '反洗钱系统'}]
    req = {
        'title': '反洗钱人行重点指标查询'
        , 'start_date': start_date
        , 'end_date': end_date
        , 'req': list_req
    }
    print(req)
    return render(request, 'trans_fxq_report/index.html', req)

import json
import configparser
from django.views.decorators.csrf import csrf_exempt    #可post调用url


list_data = []
err_list = []
class forThread(threading.Thread):
    def __init__(self, event):
        threading.Thread.__init__(self)
        self.name = 'myThread'
        self.event = event

    def run(self):
        #if self.event.get('bank_group') == self.event.get('line_data').get('_name_ch'):
        err_list = []
        print(self.event.get('start_date') + '---' + self.event.get('end_date'))
        resp = shell.getKey('check[run_command:user:./aml/report/get_rhjc.sh:' +
                            self.event.get('start_date') +
                            ':' + self.event.get('end_date') +
                            ']', self.event.get('line_data').get('_ip'), self.event.get('line_data').get('_port'))

        try:
            print(resp[1].decode('GBK'))
            info = resp[1].decode('GBK').split('\n')
        except:
            info = resp[1].split('\n')

        # print(info)

        err_list_tmp = []
        try:
            for line_info in info:
                if line_info != '':
                    if line_info.startswith('RETURN') == True:
                        print(line_info)
                        if line_info.startswith('RETURN_DECBJY_COUNT:') == True:
                            DECBJY_COUNT = int(float(line_info.lstrip('RETURN_DECBJY_COUNT:')))
                        if line_info.startswith('RETURN_DEJY_COUNT:') == True:
                            DEJY_COUNT = int(float(line_info.lstrip('RETURN_DEJY_COUNT:')))
                        if line_info.startswith('RETURN_DELBSJB_COUNT:') == True:
                            DELBSJB_COUNT = int(float(line_info.lstrip('RETURN_DELBSJB_COUNT:')))
                        if line_info.startswith('RETURN_DECBSJB_COUNT:') == True:
                            DECBSJB_COUNT = int(float(line_info.lstrip('RETURN_DECBSJB_COUNT:')))
                        if line_info.startswith('RETURN_DESJB_COUNT:') == True:
                            DESJB_COUNT = int(float(line_info.lstrip('RETURN_DESJB_COUNT:')))
                        if line_info.startswith('RETURN_KHSBCQ_COUNT:') == True:
                            KHSBCQ_COUNT = int(float(line_info.lstrip('RETURN_KHSBCQ_COUNT:')))
                        if line_info.startswith('RETURN_XKFXPJCQ_COUNT:') == True:
                            XKFXPJCQ_COUNT = int(float(line_info.lstrip('RETURN_XKFXPJCQ_COUNT:')))
                        if line_info.startswith('RETURN_CLFXPJCQ_COUNT:') == True:
                            CLFXPJCQ_COUNT = int(float(line_info.lstrip('RETURN_CLFXPJCQ_COUNT:')))
                        if line_info.startswith('RETURN_KYALCLCQ_COUNT:') == True:
                            KYALCLCQ_COUNT = int(float(line_info.lstrip('RETURN_KYALCLCQ_COUNT:')))
                        if line_info.startswith('RETURN_KYALBSL_COUNT:') == True:
                            KYALBSL_COUNT = float(line_info.lstrip('RETURN_KYALBSL_COUNT:'))
                    else:
                        err_list_tmp.append(line_info + '</br>')


            print("DECBJY_COUNT = %d DEJY_COUNT = %d DELBSJB_COUNT = %d DECBSJB_COUNT = %d DESJB_COUNT = %d" % (
                DECBJY_COUNT, DEJY_COUNT, DELBSJB_COUNT, DECBSJB_COUNT, DESJB_COUNT))
            print("KHSBCQ_COUNT = %d XKFXPJCQ_COUNT = %d CLFXPJCQ_COUNT = %d KYALCLCQ_COUNT = %d KYALBSL_COUNT = %.2f" % (
            KHSBCQ_COUNT, XKFXPJCQ_COUNT, CLFXPJCQ_COUNT, KYALCLCQ_COUNT, KYALBSL_COUNT))

            #大额交易迟报率
            DECBL = "%d" % (DECBJY_COUNT / DEJY_COUNT * 100)

            #数据包漏报率
            LBL = "%d" % (DELBSJB_COUNT / DESJB_COUNT * 100)

            #客户识别超期未处理
            #KHSBCQ = KHSBCQ_COUNT

            #新开风险评级未处理
            #XKFXPJCQ = XKFXPJCQ_COUNT

            # 存量风险评级未处理
            #CLFXPJCQ = CLFXPJCQ_COUNT


        except:
            DECBJY_COUNT = -1
            DEJY_COUNT = -1
            DELBSJB_COUNT = -1
            DECBSJB_COUNT = -1
            DESJB_COUNT = -1

            KHSBCQ_COUNT = -1
            XKFXPJCQ_COUNT = -1
            CLFXPJCQ_COUNT = -1
            KYALCLCQ_COUNT = -1
            KYALBSL_COUNT = -1

            DECBL = 0
            LBL = 0
            #KHSBCQ=0
            #XKFXPJCQ=0
            #CLFXPJCQ=0


            err_list.extend(err_list_tmp)

        # print(info_list)
        # print(oper_list)

        if err_list == []:
            err_list.append('0')

        print(err_list)

        dict_data = {
            "_name": self.event.get('line_data').get('_name')
            , "_name_ch": self.event.get('line_data').get('_name_ch')
            , "DECBL": DECBL
            , "LBL": LBL
            , "KYALBSL_COUNT": KYALBSL_COUNT
            , "KHSBCQ_COUNT": KHSBCQ_COUNT
            , "XKFXPJCQ_COUNT": XKFXPJCQ_COUNT
            , "CLFXPJCQ_COUNT": CLFXPJCQ_COUNT
            , "KYALCLCQ_COUNT": KYALCLCQ_COUNT



            , "err_list": err_list
        }
        list_data.append(dict_data)







# 一级交易查询---本地查询
@csrf_exempt
def post(request):
    print('start post')
    print(request.POST)  # form 包含提交的数据
    print(request.POST.get('date'))
    print(request.POST.get('bank_id'))
    f = open('/home/insp_ap/inspect/src/switch/' + 'aml_server' + '/config.ini', 'r', encoding='gbk')

    n = 1
    list_data.clear()
    err_list.clear()
    for line in f.readlines():
        line = line.rstrip('\n')
        if line.startswith('#') != True:
            line_data = swinit.swInit(line)
            #if line_data.get('_name') == 'PCNK':
            input_data = {
                    "start_date": request.POST.get('start_date')
                    , "end_date": request.POST.get('end_date')
                    , "line_data": line_data
                }
            exec('thread{} = forThread(input_data)'.format(n))
            exec('thread{}.start()'.format(n))
            print(input_data)
            n += 1



    print('n = ' + str(n))
    x = 1
    while x < n :
        exec('thread{}.join()'.format(x))
        x += 1


    list_data.sort(key=lambda item: item.get('err_list'), reverse=True)

    resp = {
        "code": 0,
        "msg": ",",
        "count": n,
        "data": list_data
    }
    #print(resp)
    return HttpResponse(json.dumps(resp), content_type="application/json")

# 二级交易查询---联动查询
@csrf_exempt
def postTrans(request):
    print('start post')
    print(request.POST)  # form 包含提交的数据
    bank_info = []
    bank_info = request.POST.getlist('bank_info[]')
    oper_info = request.POST.getlist('oper_info[]')
    err_list = request.POST.getlist('err_list[]')

    print(type(bank_info))
    print(bank_info)
    # time.sleep(2)
    resp = {
        "未签退机构信息": '</br>' + '</br>'.join(bank_info) + '</br>'
        , "未签退柜员信息": '</br>' + '</br>'.join(oper_info) + '</br>'
        , "报错信息": '</br>' + ''.join(err_list) + '</br>'
        , "BANK_NAME": request.POST.getlist('_name_ch')
    }
    return HttpResponse(json.dumps(resp), content_type="application/json")


