#-*- coding: utf-8 *-


import subprocess

class Shell(object):
    def runCmd(self, cmd):
        # cmd = cmd.encode('utf-8')
        print('run_cmd:' + cmd)
        res = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        sout, serr = res.communicate()
        return res.returncode, sout, serr, res.pid

    def getKey(self, cmd, ip, port):
        res = subprocess.Popen('~/bin/zabbix_get -s "' + ip + '" -p' + port + ' -k"' + cmd + '"', shell=True,
                               stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        sout, serr = res.communicate()
        return res.returncode, sout, serr, res.pid
        # print("返回码：" + result[0])
        # print("标准输出：" + result[1])
        # print("标准错误：" + result[2])

# class Get(object):
#     def keyValue(self, key, date):
#         resp_code='ERR'
#         try:
#             result = shell.getKey('check[run_command:user:./gdxy/' + key + ':hostname:' + date + ']',
#                                   line.split(':')[4], line.split(':')[8].rstrip('\n'))
#             if result[1].decode('gbk').find('RETURN:OK') != -1:
#                 resp_code = 'OK'
#             else:
#                 resp_code = 'ERR'
#         except:
#             resp_code = 'ERR'
#         return resp_code

class Public(object):
    def swInit(self, line):
        try:
            _type = line.split(':')[9]
        except:
            _type = ''
        return {
            "_name_ch": line.split(':')[0]
            , "_name": line.split(':')[1]
            , "_user": line.split(':')[2]
            , "_ver": line.split(':')[3]
            , "_ip": line.split(':')[4]
            , "_passwd": line.split(':')[5]
            , "_team": line.split(':')[6]
            , "_worker": line.split(':')[7]
            , "_port": line.split(':')[8]
            , "_type": _type
        }

def getConnInfo():
    return 'insp_ap/insp_ap@163.1.6.40/orcl'

from myview.models import Article
import time
def add_count():
    r = Article(
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        , user = 'FXB'
        , html_id = 'home'
        , html_title = '兴业数金鲲鹏管理平台'
        , browser_name = 'Google Chrome'
        , connect_type = '1'
    )
    print(r)
    r.save()
    return True


def auth_net(request):
    print('run main.auth_net')
    add_count()
    if request.META.get('REMOTE_ADDR')[0:9] == '163.11.1.':
        print('合法地址[' + request.META.get('REMOTE_ADDR') + ']')
        return True
    else :
        print('非法地址[' + request.META.get('REMOTE_ADDR') + ']')
        return False

# 权限检查
#     resp_auth = main.auth(request, False, True, 'rjxf_make')
#     if resp_auth[0] == False:
#         return render(request, 'alarm/resp.html', {"message": resp_auth[1]})

# def auth(request, net, login, perm):
#     print('in auth')
#     print('net   = ' + str(net))
#     print('login = ' + str(login))
#     print('ip    = ' + request.META.get('REMOTE_ADDR')[0:9])
#     add_count()
#     user = request.user
#     if net == True and request.META.get('REMOTE_ADDR')[0:9] != '163.11.1.':
#         return False, '该功能需要在生产终端上才可以访问哟：）'
#     print(user.is_authenticated)
#     if login == True and user.is_authenticated != True:
#         return False, '该功能需要登陆才能访问：）'
#     elif perm != '' and user.has_perm(perm) != True:
#         return False, '您没有使用该功能的权限：）'
#     else:
#         print('权限检查通过')
#         return True, '权限检查通过'

from django.contrib.auth.models import Group

# 权限检查
# auth_data = {
#     'request': request
#     , 'net': False        # 为 True 则限制办公环境功能
#     , 'net_sc': False     # 为 True 则限制生产终端功能
#     , 'login': False      # 为 True 则限制必则登陆
#     , 'debug': False
#     , 'perm': 'rjxf_make' # 权限检查
#     , 'perm_group': '知识库管理员'
# }
# resp_auth = main.auth(auth_data)
# if resp_auth.get('code') == False:
#     return render(request, 'alarm/resp.html', {"message": resp_auth.get('msg')})
def auth(data):
    print('in auth')
    print('net   = ' + str(data.get('net')))
    print('login = ' + str(data.get('login')))
    print('ip    = ' + data.get('request').META.get('REMOTE_ADDR')[0:9])

    add_count()
    user = data.get('request').user
    code = False
    net = data.get('net')
    login = data.get('login')
    # net = True
    login = True

    print(data.get('request').path)
    if data.get('debug') == True : net = False
    # if data.get('request').path == '/rjxf_server/show/' : net = False

    list_user_group = []
    try:
        for line_group in Group.objects.filter(user=user):
            list_user_group.append(line_group.name)
    except:
        list_user_group = []

    if net == True and data.get('request').META.get('REMOTE_ADDR')[0:9] != '163.11.1.':
        msg = '该功能需要在生产终端上才可以访问哟：）'
        print(user.is_authenticated)
    elif data.get('net_sc') == True and data.get('request').META.get('REMOTE_ADDR')[0:9] == '163.11.1.':
        msg = '该功能禁止在生产终端上使用：）'
        print(user.is_authenticated)
    elif login == True and user.is_authenticated != True:
        msg = '该功能需要登陆才能访问：）'
    elif data.get('perm') != '' and user.has_perm(data.get('perm')) != True:
        msg = '您没有使用该功能的权限：）'
    elif data.get('perm_group') not in ['', None] and data.get('perm_group') not in list_user_group:
        msg = '您无[' + data.get('perm_group') + ']该功能的权限：）'
    else:
        print('权限检查通过')
        code = True
        msg = '权限检查通过'

    resp_msg = {'code': code, 'msg': msg}
    print(resp_msg)


    return resp_msg

import pymysql
def connect_mysql(sql):
    print('连接 mysql 数据库')
    conn = pymysql.connect(
        host="163.1.6.40"
        , user="root", password="Cibwh1685/",
        database="insp_ap",
        charset="utf8")

    cursor = conn.cursor()

    # print('mysql 执行SQL：')
    # print(sql)

    cursor.execute(sql)

    data = cursor.fetchall()

    conn.close()

    # print('mysql 返回结果：')
    # for line in data:
    #     print(line)
    return data

from cmdb.models import action, action_type, action_app_type, user_info

# main.action_log(request, {
#     "app_type": "search_problem"
#     , 'action_type': "show"
#     , 'info_id': info_id
# })
from django.db.models import Sum
import datetime
def action_log(request, data):
    print('index main.py action')
    data = dict(data)
    print(data)

    data.setdefault('text', '')
    data.setdefault('info_id', 0)
    data.setdefault('oper', request.user.first_name)


    y = action_type.objects.get(code=data.get('action_type'))
    score = y.score

    # 计算该项今日得分---当日限额
    date = datetime.datetime.now().date()
    count_data = action.objects.filter(
        oper=data.get('oper')
        , app_type=action_app_type.objects.get(code=data.get('app_type'))
        , action_type=action_type.objects.get(code=data.get('action_type'))
        , date__gte=date
    ).aggregate(Sum('score'))
    try:
        if count_data.get('score__sum') >= y.score_limit_day:
            score = 0
    except:
        print(score)

    # print("data.get('text') = " + data.get('text'))
    r = action(
        app_type=action_app_type.objects.get(code=data.get('app_type'))
        , action_type=action_type.objects.get(code=data.get('action_type'))
        , info_id=data.get('info_id')
        , text=data.get('text')
        , oper=data.get('oper')
        , date=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        , score=score
    )
    r.save()

    x = user_info.objects.get(first_name=data.get('oper'))
    x.score += score
    x.save()

    return 0