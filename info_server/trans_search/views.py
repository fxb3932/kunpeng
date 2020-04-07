from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import time
import threading

import sys
sys.path.append('../')
import main




shell = main.Shell()
swinit = main.Public()
# _ip = '163.51.1.10'
# _port = '10066'
def index(request):
    print('start index')
    s_date = time.strftime('%Y-%m-%d', time.localtime())
    list_req = [{'bank_id': 'v3_cib', 'bank_name': 'V3核心'}]
    req = {
        'title': 'V3核心日结查询'
        , 'date': s_date
        , 'req': list_req
    }
    return render(request, 'chkpcl_server/index.html', req)

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
        resp = shell.getKey('check[run_command:user:./chkpcl/check_stat.sh:' +
                            self.event.get('date') +
                            # '2019-07-16' +
                            '@' + self.event.get('line_sub') +
                            ']', self.event.get('line_data').get('_ip'), self.event.get('line_data').get('_port'))

        try:
            info = resp[1].decode('GBK').split('\n')
        except:
            info = resp[1].split('\n')

        # print(info)

        err_list_tmp = []
        for line_info in info:
            if line_info != '':
                if line_info.startswith('RETURN:') == True:
                    if line_info.startswith('RETURN:ALL:') == True:
                        stat_all = int(float(line_info.lstrip('RETURN:ALL:')))
                    if line_info.startswith('RETURN:ERR:') == True:
                        stat_err = int(float(line_info.lstrip('RETURN:ERR:')))
                    if line_info.startswith('RETURN:OK:') == True:
                        stat_ok = int(float(line_info.lstrip('RETURN:OK:')))
                    if line_info.startswith('RETURN:DEF:') == True:
                        stat_def = int(float(line_info.lstrip('RETURN:DEF:')))
                else:
                    err_list_tmp.append(line_info + '</br>')

        try:
            print("stat_all = %d stat_err = %d stat_ok = %d stat_def = %d" % (stat_all, stat_err, stat_ok, stat_def))
            # print("stat_all = %d" % (stat_all))
            # print("stat_err = %d" % (stat_err))
            # print("stat_ok = %d" % (stat_ok))
            # print("stat_def = %d" % (stat_def))
        except:
            stat_all = -1
            stat_err = -1
            stat_ok = -1
            stat_def = -1
            err_list.extend(err_list_tmp)

        if stat_def > 0:
            gdxy_pcl_stat = '未完成'
        elif stat_def < 0:
            gdxy_pcl_stat = '未知状态'
        else:
            gdxy_pcl_stat = '已完成'

        if stat_all == 0:
            cib_pcl_stat = '未开始'
        elif stat_err < 0:
            cib_pcl_stat = '未知状态'
        elif stat_err > 0:
            cib_pcl_stat = '批处理中断'
        elif stat_ok != stat_all:
            cib_pcl_stat = '进行中'
        elif stat_ok == stat_all:
            cib_pcl_stat = '已完成'
        if stat_all == 0:
            resp = shell.getKey('check[run_command:user:./chkpcl/check_bank.sh:' +
                                self.event.get('date') +
                                '@' + self.event.get('line_sub') +
                                ']', self.event.get('line_data').get('_ip'),
                                self.event.get('line_data').get('_port'))
            try:
                info = resp[1].decode('GBK').split('\n')
            except:
                info = resp[1]
            # print(info)
            info_list = []
            for line_info in info:
                if line_info != '':
                    if line_info.startswith('RETURN:') == True:
                        info_list.append(line_info.lstrip('RETURN:'))
                    else:
                        err_list.append(line_info + '</br>')

            oper_list = []
            resp = shell.getKey('check[run_command:user:./chkpcl/check_oper.sh:' +
                                self.event.get('date') +
                                '@' + self.event.get('line_sub') +
                                ']', self.event.get('line_data').get('_ip'),
                                self.event.get('line_data').get('_port'))
            try:
                info = resp[1].decode('GBK').split('\n')
            except:
                info = resp[1]
            # print(info)
            oper_list = []
            for line_info in info:
                if line_info != '':
                    if line_info.startswith('RETURN:') == True:
                        oper_list.append(line_info.lstrip('RETURN:'))
                    else:
                        err_list.append(line_info + '</br>')
        else:
            info_list = []
            oper_list = []
            gdxy_pcl_stat = '已完成'

        # print(info_list)
        # print(oper_list)

        if err_list == []:
            err_list.append('0')
        dict_data = {
            "_name": self.event.get('line_data').get('_name')
            , "_name_ch": self.event.get('line_data').get('_name_ch')
            , "bank_name": self.event.get('bank_name')
            , "bank_id": self.event.get('bank_id')
            , "bank_no": self.event.get('line_sub')
            , "count_banknologin": len(info_list)
            , "count_opernologin": len(oper_list)
            , "gdxy_pcl_stat": gdxy_pcl_stat
            , "cib_pcl_stat": cib_pcl_stat
            , "bank_info": info_list
            , "oper_info": oper_list
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
    f = open('/home/insp_ap/inspect/src/switch/' + request.POST.get('bank_id') + '/config.ini', 'r', encoding='gbk')
    #f = open('/home/insp_ap/inspect/src/switch/' + request.POST.get('bank_id') + '/config.ini.test', 'r', encoding='gbk')
    conf = configparser.ConfigParser()
    conf.read('/home/insp_ap/inspect/src/switch/v3_cib/discovery.ini', encoding='gbk')  # 文件路径


    n = 1
    list_data.clear()
    err_list.clear()
    for line in f.readlines():
        line = line.rstrip('\n')
        if line.startswith('#') != True:
            line_data = swinit.swInit(line)
            #print(line_data['_ip'] + ' ' + line_data['_port'])
            for line_sub in conf.sections():
                if conf.get(line_sub, "bank_group") == line_data.get('_name_ch'):
                    input_data = {
                        "date": request.POST.get('date')
                        , "line_sub": line_sub
                        , "line_data": line_data
                        , "bank_name": conf.get(line_sub, "bank_name")
                        , "bank_id": conf.get(line_sub, "bank_id")
                        , "bank_group": conf.get(line_sub, "bank_group")
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







    # b.jgdh, a.jygy, a.hcgy, a.jzgylsh, a.hcgylsh, b.zfjylsh, a.bdclzt,
    # (select d.dict_info from gapsdb30:t_dict d where d.dict_key=a.bdclm and d.dict_kind='dlde_bwzt'),
    # b.ylxz, b.jyje
    #print(list_data)
    list_data.sort(key=lambda item: item.get('count_opernologin'), reverse=True)
    list_data.sort(key=lambda item: item.get('count_banknologin'), reverse=True)
    #print(list_data)
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


