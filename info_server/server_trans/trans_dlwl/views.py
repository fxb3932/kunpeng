from django.shortcuts import render
import sys
from django.http import HttpResponse
import subprocess


class Shell(object):
    def runCmd(self, cmd):
        res = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        sout, serr = res.communicate()
        return res.returncode, sout, serr, res.pid

    def getKey(self, cmd, ip, port):
        res = subprocess.Popen('~/bin/zabbix_get -s "' + ip + '" -p' + port + ' -k"' + cmd + '"', shell=True,
                               stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        print("~/bin/zabbix_get -s " + ip + " -p" + port + "-k" + cmd)
        sout, serr = res.communicate()
        return res.returncode, sout, serr, res.pid
        # print("返回码：" + result[0])
        # print("标准输出：" + result[1])
        # print("标准错误：" + result[2])

import pymysql.cursors
def index(request):
    list=[]

    # 连接数据库
    connection = pymysql.connect(host='163.1.6.40',
                                 user='root',
                                 password='Cibwh1685/',
                                 db='insp_ap',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            # 读取单条记录
            sql = "SELECT distinct bank_name from trans_dlwl_chnltrans;"
            cursor.execute(sql)
            result = cursor.fetchall()
            for line in result:
                #print(line.get('bank_name'))
                list.append(line.get('bank_name'))
    finally:
        connection.close()

    req = {
        'title': '代理网联交易查询',
        'date': '',
        'list': list
    }
    return render(request, 'trans_dlwl/index.html', req)


def index2(request):
    print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    # info_dict = {'one': 'zixue', 'two': 'IT'}
    # req = {
    #     'title': '代理网联交易分析',
    #     'date': "20190731",
    #     'req': info_dict
    # }

    dBankInfo = {
        'dlzf_hd': {"name": '兴业银行代理网联', 'ip': '163.51.1.13', 'port': '10066'},
        'dlzf': {"name": '邯郸银行代理网联', 'ip': '163.51.1.14', 'port': '10066'}
    }
    print(dBankInfo.get('dlzf').get('name'))
    shell = Shell();
    ip = dBankInfo.get('dlzf').get('ip')
    port = dBankInfo.get('dlzf').get('port')
    msg = shell.getKey('check[run_command:user:get_dlwl\/get_dlwl.sh]', ip, port)

    try:
        info = msg[1].decode('GBK').split('\n')
    except:
        info = msg[1]
    list = [];
    for line in info:
        if line.startswith('RETURN:') == True:
            sBankName = line.split(':')[1]
            # print(sBankName)
            list.append(sBankName)
    #print(list)
    #rep={'req':list}
    req = {
        'title': '代理网联交易查询',
        'date': '',
        'list': list
    }
    return render(request, 'trans_dlwl/index.html', req)


import json
from django.views.decorators.csrf import csrf_exempt    #可post调用url
@csrf_exempt
def post_data(request):
    data_get= request.POST;
    mydict={
        'name':'huiayang',
        'age':'999'
    }
    print('----------------------------')
    print(data_get)
    print('----------------------------')
    dict={
        'title':"测试实例",
        'tran_name':["衬衫1","羊毛衫2","雪纺衫","裤子","高跟鞋","袜子"],
        'tran_value':[5, 20, 36, 10, 10, 50],
        'tran_type':'交易量'

    }

    # if data_get.sBankName.isspace() == True:
    #         dict.get('tran_name') =["衬23","11衫2","雪纺23衫","裤子","高跟鞋","袜子"]
    resp_dict=json.dumps(dict)
    #return HttpResponse(resp_dict)

    #return HttpResponse(resp_dict,content_type="text/plain")
    print(dict)

    return HttpResponse(resp_dict,content_type="application/json")
