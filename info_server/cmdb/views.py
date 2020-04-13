from django.shortcuts import render
import sys
sys.path.append('../')
import main
# Create your views here.
list_req = [
    {'bank_id': 'aml_server', 'bank_name': '反洗钱SERVER', 'config_file': 'config.ini'}
    , {'bank_id': 'aml_web', 'bank_name': '反洗钱WEB', 'config_file': 'config.ini'}
    , {'bank_id': 'cib', 'bank_name': 'V2核心系统', 'config_file': 'config.ini'}
    , {'bank_id': 'v3_cib', 'bank_name': 'V3核心系统', 'config_file': 'config.ini.cmdb'}
    , {'bank_id': 'sgb_server', 'bank_name': 'SGB', 'config_file': 'config.ini'}
    , {'bank_id': 'fib_server', 'bank_name': '数据交换', 'config_file': 'config.ini'}
    , {'bank_id': 'fib_root', 'bank_name': '综合报表', 'config_file': 'config.ini'}
    , {'bank_id': 'fib_sjtq', 'bank_name': '商行数据提取', 'config_file': 'config.ini'}
    , {'bank_id': 'east_server', 'bank_name': 'EAST', 'config_file': 'config.ini'}
    , {'bank_id': 'topfe_server', 'bank_name': '金卡前置', 'config_file': 'config.ini'}
    , {'bank_id': 'topfev3_server', 'bank_name': 'V3金卡前置', 'config_file': 'config.ini'}
    , {'bank_id': 'cams_server', 'bank_name': 'V2集中账户', 'config_file': 'config.ini'}
]
def index(request):
    print('start cmdb index')

    # 权限检查
    auth_data = {
        'request': request
        , 'net': False
        , 'login': True
        , 'perm': 'rjxf_make'
    }
    resp_auth = main.auth(auth_data)
    if resp_auth.get('code') == False:
        return render(request, 'alarm/resp.html', {"message": resp_auth.get('msg')})




    req = {
        'title': 'CMDB配置操作',
        'req': list_req
    }
    # print(req)
    return render(request, 'cmdb/index.html', req)


from django.views.decorators.csrf import csrf_exempt    #可post调用url

from cmdb.models import config
from django.http import HttpResponse
shell = main.Shell()
swinit = main.Public()
import json
@csrf_exempt
def post(request):
    print('start post')
    print(request.POST)  # form 包含提交的数据

    print(config.objects.all())
    plat_name = ''
    for line in list_req:
        if line.get('bank_id') == request.POST.get('bank_id'):
            plat_name = line.get('bank_name')
            config_file = line.get('config_file')


    config.objects.filter(plat_id=request.POST.get('bank_id')).delete()
    n_ok = 0
    n_err = 0
    f = open('/home/insp_ap/inspect/src/switch/' + request.POST.get('bank_id') + '/' + config_file, 'r', encoding='gbk')
    for line in f.readlines():
        line = line.rstrip('\n')
        if line.startswith('#') != True:
            line_data = swinit.swInit(line)
            print(line_data.get('_name_ch'))
            r = config(
                plat_id=request.POST.get('bank_id')
                , plat_name=plat_name
                , name_ch=line_data.get('_name_ch')
                , name=line_data.get('_name')
                , user=line_data.get('_user')
                , sys=line_data.get('_ver')
                , ip=line_data.get('_ip')
                , passwd=line_data.get('_passwd')
                , team=line_data.get('_team')
                , worker=line_data.get('_worker')
                , bank=line_data.get('_bank')
                , port=line_data.get('_port')
                , ver=line_data.get('_type')
            )
            print(r)


            try:
                r.save()
                n_ok += 1
            except:
                print('error data :')
                print(line_data)
                n_err += 1





    resp = {
        "code": 0,
        "msg": "成功[" + str(n_ok) + "] 失败[" + str(n_err) + ']'
    }
    return HttpResponse(json.dumps(resp), content_type="application/json")


def config_bank(request):
    print('start config_bank')

    # 权限检查
    auth_data = {
        'request': request
        , 'net': False
        , 'login': True
        , 'perm': 'rjxf_make'
    }
    resp_auth = main.auth(auth_data)
    if resp_auth.get('code') == False:
        return render(request, 'alarm/resp.html', {"message": resp_auth.get('msg')})




    req = {
        'title': '多法人租户配置',
        'req': list_req
    }
    # print(req)
    return render(request, 'cmdb/config_bank.html', req)


import configparser
from cmdb.models import config_discovery



@csrf_exempt
def post_config_bank(request):
    print('start post_config_bank')
    print(request.POST)  # form 包含提交的数据


    # print(config.objects.all())


    # config.objects.all().delete()
    n_ok = 0
    n_err = 0
    #f = open('/home/insp_ap/inspect/src/switch/v3_cib/run/trans_mon/discovery.ini', 'r', encoding='gbk')
    conf = configparser.ConfigParser()
    conf.read('/home/insp_ap/inspect/src/switch/v3_cib/run/trans_mon/' + request.POST.get('acct_type'), encoding='gbk')
    print(conf.get('14013','bank_name'))
    print(request.POST.get('bank_id'))
    print(request.POST.get('acct_type'))
    print("所有节点==>", conf.sections())
    # config_discovery.objects.all().delete()
    config_discovery.objects.filter(plat=request.POST.get('bank_id')).delete()
    for line in conf.sections():
        # print(line)
        # print(conf.get(line, 'bank_id'))
        # print(conf.get(line, 'bank_name'))
        # print(conf.get(line, 'bank_group'))

        r = config_discovery(
            plat=request.POST.get('bank_id')
            , bank_id=conf.get(line, 'bank_id')
            , bank_no=line
            , bank_name=conf.get(line, 'bank_name')
            , bank_group=conf.get(line, 'bank_group')
        )
        # print(r)
        try:
            r.save()
            n_ok += 1
        except:
            n_err += 1




    resp = {
        "code": 0,
        "msg": "成功[" + str(n_ok) + "] 失败[" + str(n_err) + ']'
    }
    return HttpResponse(json.dumps(resp), content_type="application/json")

def cmdb_plat_info(request):
    print('start cmdb_plat_info index')

    # 权限检查
    auth_data = {
        'request': request
        , 'net': False
        , 'login': True
        , 'debug': True
        , 'perm': 'rjxf_make'
    }
    resp_auth = main.auth(auth_data)
    if resp_auth.get('code') == False:
        return render(request, 'alarm/resp.html', {"message": resp_auth.get('msg')})

    req = {
        'title': 'CMDB配置操作'
    }
    # print(req)
    return render(request, 'cmdb/cmdb_plat_info.html', req)

from .models import i_plat
from .models import c_config2
from .models import i_bank
from .models import i_app_server
# from .models import c_config_bank
from .models import i_app_stat
@csrf_exempt
def get_plat_info(request):
    print('start get_plat_info index')

    data = []

    set_plat_id = set({})

    for line in i_plat.objects.all():
        set_plat_id.add(line.plat_id)

    # 按产品分行
    for line_set_plat_id in set_plat_id :
        print(line_set_plat_id)

        # 按 V2、V3 分类
        v2_count = 0
        v3_count = 0
        for line_i_plat in i_plat.objects.filter(plat_id=line_set_plat_id):
            print(line_i_plat.plat_ver)
            data_i_plat = line_i_plat
            if line_i_plat.plat_ver.name == 'V2':
                v2_count += 1
            if line_i_plat.plat_ver.name == 'V3':
                v3_count += 1

        bank_stat_0_count = 0
        bank_stat_1_count = 0
        for line in c_config.objects.filter(plat__plat_id=line_set_plat_id):
            print(line.app_stat.stat_id)
            if line.app_stat.stat_id == 0:
                bank_stat_0_count += 1
            if line.app_stat.stat_id == 1:
                bank_stat_1_count += 1

        bank_not_set = 0
        for line in i_bank.objects.all():
            print(line.name)
            if len(c_config.objects.filter(
                    plat__plat_id=line_set_plat_id
                    ,bank__name=line.name)) == 0:
                bank_not_set += 1

            # print('a')
        data.append({
            'plat_name': data_i_plat.plat_name
            , 'plat_id': line_set_plat_id
            , 'v2_count': v2_count
            , 'v3_count': v3_count
            , 'bank_stat_0_count': bank_stat_0_count
            , 'bank_stat_1_count': bank_stat_1_count
            , 'bank_not_set': bank_not_set
        })

    print(data)
    print(data_i_plat.plat_name)

    resp = {
        'code': 0
        , 'msg': ''
        , 'data': data
    }
    return HttpResponse(json.dumps(resp), content_type="application/json")

def cmdb_input(request):
    print('start cmdb_input index')

    # 权限检查
    auth_data = {
        'request': request
        , 'net': False
        , 'login': True
        , 'debug': True
        , 'perm': 'rjxf_make'
    }
    resp_auth = main.auth(auth_data)
    if resp_auth.get('code') == False:
        return render(request, 'alarm/resp.html', {"message": resp_auth.get('msg')})

    # 所属产品
    plat_info = []

    for line in i_plat.objects.all():
        plat_info.append({
            'plat_id': line.plat_ver.name + '-' + line.plat_id
            , 'plat_name': line.plat_ver.name + '-' + line.plat_id + '-' + line.plat_name
        })

    # 所属服务器
    sys_info = []
    for line in i_app_server.objects.all():
        sys_info.append({
            'id': line.ip + '-' + line.user
            , 'name': line.ip + '-' + line.user
        })

    # 合作行
    bank_info = []
    for line in i_bank.objects.all():
        bank_info.append({
            'id': line.name
            , 'name': line.name + '-' + line.name_ch
        })

    req = {
        'title': '运维对象配置'
        , 'plat_info': plat_info
        , 'sys_info': sys_info
        , 'bank_info': bank_info
    }
    print(req)
    return render(request, 'cmdb/cmdb_input.html', req)