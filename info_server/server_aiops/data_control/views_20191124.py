from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt  # 可post调用url
import json

# Create your views here.
import main
from cmdb.models import config
import time


def index(request):
    print('start index data_control')

    # 权限检查
    auth_data = {
        'request': request
        , 'net': False
        , 'login': True
        , 'debug': True
        , 'perm': ''
    }
    resp_auth = main.auth(auth_data)
    if resp_auth.get('code') == False: return render(request, 'alarm/resp.html', {"message": resp_auth.get('msg')})

    plat_list = [
        {'plat_id': 'cib', 'plat_name': 'V2核心系统'}
        # , {'plat_id': 'v3_cib', 'plat_name': 'V3核心系统'}
    ]
    cmdb_data = config.objects.filter(plat_id='cib')

    bank_list = []
    bank_list.clear()
    for line in cmdb_data:
        if line.name_ch[-4:] != '_CLJ':
            bank_list.append({
                'name': line.name
                , 'name_ch': line.name_ch
            })

    # for line in config.objects.filter(plat_id='v3_cib'):
    #     if line.name_ch[-4:] != '_CLJ':
    #         bank_list.append({
    #             'name': line.name
    #             , 'name_ch': line.name_ch
    #         })

    user = request.user
    req = {
        'title': '数据文件载入'
        , 'user_name': user.username
        , 'date': time.strftime('%Y%m%d', time.localtime())
        , 'bank_list': bank_list
        , 'plat_list': plat_list
    }
    # print(req)
    return render(request, 'data_control/index.html', req)

import os
shell = main.Shell()
file_path = '/home/insp_ap/rjxf/data_control/file/'
key_path = '/home/insp_ap/rjxf/data_control/key/'
@csrf_exempt
def get_file_info(request):
    print('start get_file_info function')
    print(request.POST.get('plat_id'))
    print(request.POST.get('bank_id'))
    print(request.POST.get('file_name1'))
    file_name = request.POST.get('bank_id') + '_' + request.POST.get('file_name1').split('/')[-1]

    cmdb_data = config.objects.filter(
        # plat_id='cib'
        plat_id=request.POST.get('plat_id')
        , name=request.POST.get('bank_id')
    )
    # print(list(cmdb_data))

    resp1 = []
    file_size = 0
    code = 0
    msg = {
        'file': '未处理'
        , 'key': '未处理'
        , 'enc': '未处理'
    }
    key_ctime = ''
    enc_file_name = ''
    for line in cmdb_data:
        print(line)
        print(line.ip)

        # 文件载入
        cmd = 'scp cib@' + line.ip + ':' + request.POST.get('file_name1') + ' ' + file_path + file_name
        resp1 = shell.runCmd(cmd)
        if resp1[0] != 0:
            msg['file'] = '文件加载失败'
            code = -1

        # 获取文件基本信息
        try:
            fileinfo = os.stat(file_path + file_name)  # 获取文件的基本信息
            msg['file'] = '正常，文件大小 ' + str(fileinfo.st_size)
        except:
            print('文件信息获取失败')
            msg['file'] = '文件信息获取失败'
            code = -1

        # 获取公钥文件信息
        try:
            key_name = key_path + line.name + '_publickey.pem'
            keyinfo = os.stat(key_name)
            key_ctime_sec = time.localtime(keyinfo.st_ctime)  # 秒数
            msg['key'] = '正常，密钥日期 ' + time.strftime("%Y-%m-%d %H:%M:%S", key_ctime_sec)
        except:
            print('公钥信息获取失败')
            msg['key'] = '公钥信息获取失败'
            code = -2

        # 使用公钥加密文件生成
        enc_file = file_path + file_name + '.enc'
        cmd = 'openssl smime -encrypt -aes256 ' \
              ' -in ' + file_path + file_name + \
              ' -binary -outform DEM -out ' + enc_file + ' ' + key_name
        resp2 = shell.runCmd(cmd)
        if resp2[0] != 0:
            msg['enc'] = '文件加密失败'
            code = -1
        else :
            msg['enc'] = resp2[1].decode('gbk')

        try:
            encinfo = os.stat(enc_file)
            msg['enc'] = '正常，文件大小 ' +  str(encinfo.st_size)
            enc_file_name = enc_file.split('/')[-1]
        except:
            print('加密文件信息获取失败')
            msg['enc'] = '加密文件信息获取失败'
            enc_file_name = '加密文件信息获取失败'
            code = -3

    table_data = {
        'file_name': file_name
        , 'file_size': file_size
        , 'update_date': ''
#        , 'stat': resp1[1].decode('gbk')
    }

    resp = {
        'code': code
        , 'msg': msg
        , 'file_name': request.POST.get('file_name1')
        , 'key_ctime': key_ctime
        , 'enc_file': enc_file_name
        , 'table_data': table_data
    }
    return HttpResponse(json.dumps(resp), content_type="application/json")

@csrf_exempt
def data_put(request):
    # 'enc_file_name'(139639378022512) = {str}
    # 'BYDX_jkdbcsb.init.unl.enc'
    # 'plat_id'(139639378020984) = {str}
    # 'cib'
    # 'bank_id'(139639378020816) = {str}
    # 'BYDX'
    # 'file_data[file_name]'(139639594037160) = {str}
    # 'BYDX_jkdbcsb.init.unl'
    # 'file_data[file_size]'(139639593912912) = {str}
    # '0'
    # 'file_data[update_date]'(139639596967880) = {str}
    # ''
    # 'file_data[stat]'(139639378023216) = {str}
    # ''
    # 'fib_path'(139639378023472) = {str}
    # '/fib/sjtq/20191122/'

    code = 0

    # 获取数交信息

    fib_data = config.objects.filter(
        plat_id='fib_server'
        , name=request.POST.get('bank_id')
    )

    msg = {

    }
    for line in fib_data:
        print(line.ip)

        #新建目录
        cmd = 'check[run_command:user:mkdir:' + request.POST.get('fib_path') + ']'
        print(cmd)
        resp_cmd = shell.getKey(cmd, line.ip, line.port)[1].decode('gbk').rstrip('\n')
        print(resp_cmd)

        # 文件传输
        cmd = 'scp ' + file_path + request.POST.get('enc_file_name') + \
              ' fib@' + line.ip + ':' + request.POST.get('fib_path')
        resp1 = shell.runCmd(cmd)
        if resp1[0] == 0:
            msg['file'] = '正常，文件传输成功'
        else:
            msg['file'] = '文件传输失败' + resp1[1].decode('gbk')
            code = -1

    # 文件传输

    resp = {
        'code': code
        , 'msg': msg
    }
    return HttpResponse(json.dumps(resp), content_type="application/json")

