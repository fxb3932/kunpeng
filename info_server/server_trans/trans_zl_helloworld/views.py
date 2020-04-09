from cmdb.models import config
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt  # 可post调用url
import json
import time
from .models import *
from .commonutil import *

# Create your views here.
import main

stat_list_json = []
type_list_json = []
zycd_list_json = []
jjcd_list_json = []


def getListJson():
    stat_list_json.clear()
    type_list_json.clear()
    zycd_list_json.clear()
    jjcd_list_json.clear()
    ys = yything_stat(
        stat_id=1
        , stat_name="全部"
    )
    # stat_list = yything_stat.objects.filter(stat_id__gt=1)
    stat_list = yything_stat.objects.exclude(stat_id=1)
    type_list = enum_type.objects.all()
    zycd_list = enum_zycd.objects.all()
    jjcd_list = enum_jjcd.objects.all()

    for var in stat_list:
        dict_data = {
            "stat_id": var.stat_id
            , "stat_name": var.stat_name
        }
        stat_list_json.append(dict_data)

    for var in type_list:
        dict_data = {
            "type_name": var.type_name
        }
        type_list_json.append(dict_data)

    for var in zycd_list:
        dict_data = {
            "zycd_name": var.zycd_name
        }
        zycd_list_json.append(dict_data)

    for var in jjcd_list:
        dict_data = {
            "jjcd_name": var.jjcd_name
        }
        jjcd_list_json.append(dict_data)


@csrf_exempt
def showdata1(request):
    log('start showdata')
    getListJson()
    # s_date = time.strftime('%Y-%m-%d', time.localtime())
    stat_list_json.clear()
    stat_list = yything_stat.objects.all()
    for var in stat_list:
        dict_data = {
            "stat_id": var.stat_id
            , "stat_name": var.stat_name
        }
        stat_list_json.append(dict_data)
    req = {
        'title': 'abcd'
        # , 'date': s_date
        , 'stat_list_json': stat_list_json
        , 'type_list_json': type_list_json
        , 'zycd_list_json': zycd_list_json
        , 'jjcd_list_json': jjcd_list_json
    }
    return render(request, 'trans_zl_helloworld/show_data.html', req)


@csrf_exempt
def showdata2(request):
    log('start showdata2')

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

    query_date = request.POST.get('date')
    query_stat = request.POST.get('stat')
    cur_date = time.strftime('%Y-%m-%d', time.localtime())
    log("query_date :" + query_date)
    log("query_stat : " + query_stat)
    log("cur_date : " + cur_date)
    list_data = []
    response = ""
    rs = []
    if query_stat == "全部":
        rs = yything.objects.all().order_by("-submit_date")
    else:
        ys = yything_stat.objects.filter(stat_name=query_stat).first()
        rs = yything.objects.filter(t_stat=ys.stat_id).order_by("-submit_date")

    n = 0
    for var in rs:
        # ys = yything_stat.objects.filter(id=str(var.t_stat))
        # print(ys.stat_name)
        try:
            stat_str = var.t_stat.stat_name
        except:
            stat_str = ''
        try:
            type_str = var.t_type.type_name
        except:
            type_str = ''
        try:
            zycd_str = var.t_zycd.zycd_name
        except:
            zycd_str = ''
        try:
            jjcd_str = var.t_jjcd.jjcd_name
        except:
            jjcd_str = ''
        dict_data = {
            "thing_id": var.id
            , "title": var.title
            , "reason": var.reason
            , "banknames": var.banknames
            , "deal_person": var.deal_person
            , "support_org": var.support_org
            , "t_stat": stat_str
            , "t_type": type_str
            , "t_zycd": zycd_str
            , "t_jjcd": jjcd_str
            , "diffcult": var.diffcult
            , "want_date": var.want_date
            , "submit_date": var.submit_date
            , "close_date": var.close_date
            , "genjin": var.genjin
            , "yanzheng": var.yanzheng
            , "beizhu": var.beizhu
        }
        list_data.append(dict_data)
        n += 1

    resp = {
        "code": 0,
        "msg": "success",
        "count": n,
        "data": list_data
    }

    return HttpResponse(json.dumps(resp, cls=DateEncoder), content_type="application/json")


@csrf_exempt
def add_submit(request):
    log('start add_submit')
    user = request.user
    log(user)
    input_data = json.loads(request.POST.get('input_data'))
    log(input_data)
    y = yything(
        title=input_data.get('title')
        , reason=input_data.get('reason')
        , banknames=input_data.get('banknames')
        , deal_person=input_data.get('deal_person')
        , support_org=input_data.get('support_org')
        , t_stat=yything_stat.objects.get(stat_name=input_data.get('stat'))
        , diffcult=input_data.get('diffcult')
        , t_team=input_data.get('t_team')
        , beizhu=input_data.get('beizhu')
        , submit_person=str(user)
        # , want_date=input_data.get('want_date')
        # , want_date='2020-03-20 18:00:00'
        , submit_date=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        # , close_date=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    )
    if input_data.get('want_date') != '':
        y.want_date = input_data.get('want_date')

    try:
        log("ready to save")
        print(y)
        y.save()
        code = 0
        msg = '上报成功！'
    except Exception as msg_info:
        code = -1
        print(repr(msg_info))
        print(msg_info)
        msg = '提交失败了。。。<br>报错信息：' + str(msg_info)
        # msg = '录入失败了，可能该标题已存在，无法重复入库~'

    y.save()
    resp = {
        "code": code
        , "msg": msg
    }
    return HttpResponse(json.dumps(resp), content_type="application/json")


def add_data(request):
    log('start add_data')

    getListJson()

    s_date = time.strftime('%Y-%m-%d', time.localtime())

    req = {
        'title': 'abcd'
        , 'date': s_date
        , 'stat_list_json': stat_list_json
    }
    return render(request, 'trans_zl_helloworld/add_data.html', req)


@csrf_exempt
def delete_data(request, thing_id):
    log('start delete_data')
    user = request.user
    log(user)

    print('thing_id = [' + str(thing_id) + ']')
    rs = yything.objects.get(id=thing_id)

    auth_person = []
    auth_person.append("zhangyongwei")
    auth_person.append("fanbowen")
    auth_person.append(rs.submit_person)
    auth_person.append(rs.deal_person)
    print(auth_person)
    if str(user) != 'zhangyongwei' and str(user) != rs.submit_person and str(user) != rs.deal_person:
        # if auth_person.__contains__(str(user)):
        resp = {
            "code": "0"
            , "msg": "仅生产调度人员、提交人、处理人可删除！"
        }
        return HttpResponse(json.dumps(resp), content_type="application/json")

    rs.delete()
    resp = {
        "code": "0"
        , "msg": "删除成功！"
    }
    return HttpResponse(json.dumps(resp), content_type="application/json")


@csrf_exempt
def update_data(request, thing_id):
    log('start update_data')
    print('thing_id = [' + str(thing_id) + ']')
    # log("thing_id :" + thing_id)
    # print(request.POST.get('row_data'))
    # row_data = json.loads(request.POST.get('row_data'))

    rs = yything.objects.get(id=thing_id)
    print(rs)
    want_date_str = ""
    if rs.want_date is not None:
        want_date_str = rs.want_date.strftime("%Y-%m-%d %H:%M")
    log("want_date_str:" + want_date_str)
    submit_date_str = ""
    if rs.submit_date is not None:
        submit_date_str = rs.submit_date.strftime("%Y-%m-%d %H:%M")
    log("submit_date_str:" + submit_date_str)
    close_date_str = ""
    if rs.close_date is not None:
        close_date_str = rs.close_date.strftime("%Y-%m-%d %H:%M")
    log("close_date:" + close_date_str)
    beizhu_str = ""
    if rs.beizhu is not None:
        beizhu_str = rs.beizhu.replace("\n", "\\n")
    log("beizhu_str:" + beizhu_str)

    stat_name = ''
    type_name = ''
    zycd_name = ''
    jjcd_name = ''

    try:
        stat_name = rs.t_stat.stat_name
    except:
        stat_name = ''

    try:
        type_name = rs.t_type.type_name
    except:
        type_name = ''

    try:
        zycd_name = rs.t_zycd.zycd_name
    except:
        zycd_name = ''

    try:
        jjcd_name = rs.t_jjcd.jjcd_name
    except:
        jjcd_name = ''

    row_data = []
    dict_data = {
        "title": rs.title
        , "id": rs.id
        , "reason": rs.reason
        , "banknames": rs.banknames
        , "deal_person": rs.deal_person
        , "submit_person": rs.submit_person
        , "support_org": rs.support_org
        , "stat": stat_name
        , "diffcult": rs.diffcult
        , "want_date": want_date_str
        , "submit_date": submit_date_str
        , "close_date": close_date_str
        , "beizhu": beizhu_str
        , "t_team": rs.t_team
        , "t_type": type_name
        , "t_zycd": zycd_name
        , "t_jjcd": jjcd_name
        , "genjin": rs.genjin
        , "yanzheng": rs.yanzheng
    }
    print(dict_data)
    row_data.append(dict_data)

    getListJson()

    resp = {
        'title': 'modify'
        , 'row_data': dict_data
        , 'stat_list_json': stat_list_json
        , 'type_list_json': type_list_json
        , 'zycd_list_json': zycd_list_json
        , 'jjcd_list_json': jjcd_list_json
    }
    return render(request, 'trans_zl_helloworld/update_data.html', resp)


@csrf_exempt
def query_data(request, thing_id):
    log('start query_data')
    print('thing_id = [' + str(thing_id) + ']')
    # log("thing_id :" + thing_id)
    # print(request.POST.get('row_data'))
    # row_data = json.loads(request.POST.get('row_data'))

    rs = yything.objects.get(id=thing_id)
    print(rs)
    want_date_str = ""
    if rs.want_date is not None:
        want_date_str = rs.want_date.strftime("%Y-%m-%d %H:%M")
    log("want_date_str:" + want_date_str)
    submit_date_str = ""
    if rs.submit_date is not None:
        submit_date_str = rs.submit_date.strftime("%Y-%m-%d %H:%M")
    log("submit_date:" + submit_date_str)
    close_date_str = ""
    if rs.close_date is not None:
        close_date_str = rs.close_date.strftime("%Y-%m-%d %H:%M")
    log("close_date:" + close_date_str)

    stat_name = ''
    type_name = ''
    zycd_name = ''
    jjcd_name = ''

    try:
        stat_name = rs.t_stat.stat_name
    except:
        stat_name = ''

    try:
        type_name = rs.t_type.type_name
    except:
        type_name = ''

    try:
        zycd_name = rs.t_zycd.zycd_name
    except:
        zycd_name = ''

    try:
        jjcd_name = rs.t_jjcd.jjcd_name
    except:
        jjcd_name = ''

    bz_str = ''
    if rs.beizhu is not None:
        bz_str = rs.beizhu.replace("\n", "\\n")

    row_data = []
    dict_data = {
        "title": rs.title
        , "id": rs.id
        , "reason": rs.reason
        , "banknames": rs.banknames
        , "deal_person": rs.deal_person
        , "submit_person": rs.submit_person
        , "support_org": rs.support_org
        , "stat": stat_name
        , "diffcult": rs.diffcult
        , "want_date": want_date_str
        , "submit_date": submit_date_str
        , "close_date": close_date_str
        , "beizhu": bz_str
        , "t_team": rs.t_team
        , "t_type": type_name
        , "t_zycd": zycd_name
        , "t_jjcd": jjcd_name
        , "genjin": rs.genjin
        , "yanzheng": rs.yanzheng
    }
    print(dict_data)
    row_data.append(dict_data)

    getListJson()

    resp = {
        'title': 'modify'
        , 'row_data': dict_data
        , 'stat_list_json': stat_list_json
        , 'type_list_json': type_list_json
        , 'zycd_list_json': zycd_list_json
        , 'jjcd_list_json': jjcd_list_json
        , 'date_now': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    }
    return render(request, 'trans_zl_helloworld/query_data.html', resp)


@csrf_exempt
def update_submit(request, thing_id):
    log('start update_submit')
    user = request.user
    log(user)
    input_data = json.loads(request.POST.get('input_data'))
    log("input_data" + str(input_data))

    yything_stat.objects.filter(stat_name=input_data.get('stat'))

    rowdata = yything.objects.get(id=thing_id)

    input_data = json.loads(request.POST.get('input_data'))
    rowdata.title = input_data.get('title')
    rowdata.reason = input_data.get('reason')
    rowdata.banknames = input_data.get('banknames')
    rowdata.deal_person = input_data.get('deal_person')
    rowdata.t_team = input_data.get('t_team')
    rowdata.support_org = input_data.get('support_org')
    rowdata.beizhu = input_data.get('beizhu')
    rowdata.t_stat = yything_stat.objects.get(stat_name=input_data.get('stat'))
    rowdata.t_type = enum_type.objects.get(type_name=input_data.get('t_type'))
    rowdata.t_zycd = enum_zycd.objects.get(zycd_name=input_data.get('t_zycd'))
    rowdata.t_jjcd = enum_jjcd.objects.get(jjcd_name=input_data.get('t_jjcd'))
    rowdata.diffcult = input_data.get('difficult')
    if input_data.get('want_date') != '':
        rowdata.want_date = input_data.get('want_date')
    # if input_data.get('submit_date') != '':
    #     rowdata.submit_date = input_data.get('submit_date')
    if input_data.get('stat') == '已完成':
        rowdata.close_date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    if input_data.get('yanzheng') is not None:
        rowdata.yanzheng = input_data.get('yanzheng')
    else:
        rowdata.yanzheng = ''
    if input_data.get('genjin') is not None:
        rowdata.genjin = input_data.get('genjin')
    else:
        rowdata.genjin = ''

    rowdata.save()
    resp = {
        "code": "0"
        , "msg": "修改成功！"
    }
    return HttpResponse(json.dumps(resp), content_type="application/json")


shell = main.Shell()


def index(request):
    log('start index hello world')
    print(request.POST)  # form 包含提交的数据
    print(request.POST.get('zh'))

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

    bank_list = []
    s_date = time.strftime('%Y-%m-%d', time.localtime())
    # data = config.objects.all()
    data = config.objects.filter(plat_name="V2核心系统")
    for line in data:
        if line.user == 'cib':
            bank_list.append({'bank_name': line.name_ch})
            # print(bank_list)
    req = {
        'title': '冻结控制查询',
        'date': s_date,
        'req': bank_list,
    }
    print(req)
    return render(request, 'trans_zl_helloworld/index.html', req)


@csrf_exempt
def post(request):
    print('start post')
    print(request.POST)  # form 包含提交的数据

    print(request.POST.get('zh'))
    print(request.POST.get('bank_id'))
    # print(request.POST.get('bank_port'))

    zh = request.POST.get('zh')
    bank_id = request.POST.get('bank_id')
    #     ip = ''
    #     port = ''
    #     # data = config.objects.all()
    data = config.objects.filter(plat_name="V2核心系统").filter(name_ch=bank_id)
    for line in data:
        if line.user == 'cib':
            if line.name_ch == request.POST.get('bank_id'):
                ip = line.ip
                port = line.port

    log(ip + " : " + port)
    # resp = shell.getKey('check[run_command:user:ls]', ip, port)
    resp = shell.getKey('check[run_command:user:djkzxx:' +
                        zh + ']', ip, port)

    try:
        # info = resp[1].decode('GBK').split('\n')
        info = resp[1].decode('GBK')
    except:
        info = resp[1]

    n = 12

    print(info)
    resp = {
        "code": 0,
        "msg": ",",
        "count": n,
        "data": [{
            "inst_date": "1234"
            , "trans_code": "1111"
            , "query_result": info.replace('\n', '<br>')
        }]
    }
    return HttpResponse(json.dumps(resp), content_type="application/json")


def log(info):
    s_date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print('~~~~%s: %s' % (s_date, info))
