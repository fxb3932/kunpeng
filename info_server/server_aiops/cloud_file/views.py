#-*- coding: utf-8 *-

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt    #可post调用url
import json
import sys
sys.path.append('../')
import main
import sys
# import os

# os.environ['LANG'] = "en_US.UTF-8"
# os.environ['PYTHONIOENCODING'] = 'UTF-8'
# os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.ZHS16GBK'


import chardet

home_path = '/home/insp_ap/devops/info_server/static/app/cloud_file'
# _work_path = os.getcwd()

# def output_env():
#     env_dist = os.environ  # environ是在os.py中定义的一个dict environ = {}
#     # 打印所有环境变量，遍历字典
#     for key in env_dist:
#         print(key + ' : ' + env_dist[key])

# Create your views here.
def index(request):
    print('start index cloud_file')

    # 权限检查
    auth_data = {
        'request': request
        , 'net': False
        , 'login': True
        , 'debug': True
        , 'perm': ''
    }
    resp_auth = main.auth(auth_data)
    if resp_auth.get('code') == False:
        return render(request, 'alarm/resp.html', {"message": resp_auth.get('msg')})

    # print(chardet(data))



    file_path = request.GET.get('file_path')
    if file_path == None :
        file_path = '/'

    req = {
        'title': 'cloud_file'
        , 'file_path': file_path
    }
    # print(req)
    return render(request, 'cloud_file/index.html', req)

from .models import info
@csrf_exempt
def get_info(request):
    #描述 标签 评论 历史版本 操作记录 下载记录
    file_list = []
    print(request.GET.get('file_path'))

    # print(info.objects.all())
    for line in info.objects.filter(file_path=request.GET.get('file_path')) :
        file_list.append({
            'file_name': line.file_name
            , 'file_size': line.file_size
            , 'file_type': line.file_type
            , 'update_oper': line.update_oper
            , 'update_date': str(line.update_date)
            , 'file_path': line.file_path
        })

    resp = {
        "code": 0
        , "msg": ''
        , "count": 10
        , "data": file_list
    }
    return HttpResponse(json.dumps(resp), content_type="application/json")


import time
@csrf_exempt
def upload(request):
    file_obj = request.FILES.get('file', None)
    print(file_obj.name)
    print(request.GET.get('file_path'))

    # os.chdir(home_path + request.GET.get('file_path'))
    code = -1

    # 权限检查
    auth_data = {
        'request': request
        , 'net_sc': True
        , 'login': True
        , 'debug': True
        , 'perm': ''
    }
    resp_auth = main.auth(auth_data)
    if resp_auth.get('code') == False:
        resp = {"code": -1}
        return HttpResponse(json.dumps(resp), content_type="application/json")

    with open(home_path + request.GET.get('file_path') + file_obj.name, 'wb') as f:
        for line in file_obj.chunks():
            f.write(line)
        code = 0
        f.close()

    if code == 0 :
        r = info(
            file_name=file_obj.name
            , file_size=file_obj.size
            , update_oper=request.user.first_name
            , update_date=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            , file_type='f'
            , file_path=request.GET.get('file_path')
        )

        r.save()

    # code 为 0 表示上传文件成功
    resp = {
        "code": code
    }
    # os.chdir(_work_path)
    return HttpResponse(json.dumps(resp), content_type="application/json")


shell = main.Shell()

@csrf_exempt
def delete(request):
    print('index delete start')
    print(request)
    print(request.POST.get('file_name'))

    # 删除文件
    # os.chdir(home_path + request.POST.get('file_path'))
    resp = shell.runCmd('rm -rf ' + home_path + request.POST.get('file_path') + request.POST.get('file_name'))

    # 删除 info 表中记录
    r = info.objects.filter(
        file_name=request.POST.get('file_name')
        , file_path=request.POST.get('file_path')
    )
    r.delete()

    # 如果对象为目录则清理所有名下文件
    if request.POST.get('file_type') == 'd':
        for line in info.objects.all() :
            # print(line.file_type)
                if line.file_path.startswith(request.POST.get('file_path') + request.POST.get('file_name')) == True :
                    line.delete()
                    print(line.file_name + ' delete')
            # line.delete()
    # r = info.objects.filter(
    #     file_name=request.POST.get('file_name')
    #     , file_path=request.POST.get('file_path')
    # )
    # r.delete()

    resp = {
        "code": 0
    }
    # os.chdir(_work_path)
    return HttpResponse(json.dumps(resp), content_type="application/json")

@csrf_exempt
def run_mkdir(request):

    print('index run_mkdir start')
    print(request.POST.get('file_path'))
    print(request.POST.get('file_name'))
    # os.chdir(home_path + request.POST.get('file_path'))

    # file_name = request.POST.get('file_name').encode('utf-8').decode('utf-8')
    file_name = request.POST.get('file_name')
    print(file_name)
    cmd = 'mkdir ' + home_path + request.POST.get('file_path') + file_name
    shell.runCmd(cmd)
    r = info(
        file_name=request.POST.get('file_name')
        , file_size='-'
        , update_oper=request.user.first_name
        , update_date=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        , file_type='d'
        , file_path=request.POST.get('file_path')
    )

    r.save()
    resp = {
        "code": 0
    }
    # os.chdir(_work_path)
    return HttpResponse(json.dumps(resp), content_type="application/json")