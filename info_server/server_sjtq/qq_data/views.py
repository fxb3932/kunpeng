from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt  # 可post调用url
import json

# Create your views here.
import main


def index(request):
    print('start index rota_day')

    # 权限检查
    auth_data = {
        'request': request
        , 'net': False
        , 'login': True
        , 'perm': ''
    }
    resp_auth = main.auth(auth_data)
    if resp_auth.get('code') == False:
        return render(request, 'alarm/resp.html', {"message": resp_auth.get('msg')})

    req = {
        'title': 'rota_day'
    }
    # print(req)
    return render(request, 'qq_data/index.html', req)

import re
import time
from .models import info
@csrf_exempt
def upload(request):
    print('index upload')
    file_obj = request.FILES.get('file', None)
    print(file_obj.name)
    print(file_obj.size)

    info.objects.all().delete()
    t1 = time.time()

    start_flag = 0
    qq_group = ''
    qq_date = ''
    qq_oper = ''
    qq_time = ''
    qq_no = ''
    qq_data = []
    tmp_line_list = []
    for line in file_obj.readlines():
        line = str(line.decode('utf-8'))
        # line = line.replace('\n', '')
        line = line.replace('\r', '')
        line = line.replace('\n', '')

        if line.startswith('================================================================'):
            continue
        # print(line, end='\n')
        #if len(line) > 0:
        # 消息对象:清镇兴邦-运营服务
        if line.startswith('消息对象:'):
            qq_group = line.split(':')[1]
            start_flag = 1

            # print('qq_group = ' + qq_group)
            continue

        if start_flag == 2:
            # print(qq_group + ':' + qq_date + ':' + qq_oper + ':' + line)
            try:
                re.match(r'\d\d\d\d-\d\d-\d\d \d*:\d\d:\d\d ', line).span()
                # print(str(start_flag) + ':new:' + line)
                qq_data.append({
                    'group': qq_group
                    , 'date': qq_date
                    , 'time': qq_time
                    , 'oper': qq_oper
                    , 'qq_no': qq_no
                    , 'content': ' '.join(tmp_line_list)
                })
                tmp_line_list.clear()
                start_flag = 1
            except Exception as msg:
                # print(str(start_flag) + ':append:' + str(msg))
                tmp_line_list.append(line)
                continue
            # r = info(
            #     group=qq_group
            #     , date=qq_date
            #     , oper=qq_oper
            #     , content=line
            # )
            # try:
            #     r.save()
            # except:
            #     print(qq_group + ':' + qq_date + ':' + qq_oper + ':' + line)



        if start_flag == 1:
            # 2017-12-26 8:33:02 兴业金融云-服务台I(1275494344)
            try:
                re.match(r'\d\d\d\d-\d\d-\d\d \d*:\d\d:\d\d ', line).span()
                # print('ok')
                line_list = line.split(' ')
                qq_date = line_list[0]
                qq_time = line_list[1]
                try:
                    qq_no = line_list[2].split('(')[1].split(')')[0]
                    qq_oper = line_list[2].split('(')[0]
                except:
                    try:
                        qq_no = line_list[2].split('<')[1].split('>')[0]
                        qq_oper = line_list[2].split('<')[0]
                    except:
                        qq_oper = line_list[2]
                start_flag = 2
                continue
            except Exception as msg:

                # print(qq_group + ':' + qq_date + ':' + qq_oper + ':' + line + ':' + str(msg))
                if len(line) > 0:
                    print(str(start_flag) + ':' + line + ':' + str(msg))

                continue
            # print(line)


    # 用时计算
    t2 = time.time()
    t = (t2 - t1) * 1000
    print('step1 use ' + str(t))
    # 保存下发范围
    json_file_name = '/home/insp_ap/tools/qq/data.json'
    print(json_file_name)
    f_resp = open(json_file_name, 'w', encoding='utf-8')
    json.dump(qq_data, f_resp, ensure_ascii=False, indent=4)

    # 用时计算
    t3 = time.time()
    t = (t3 - t2) * 1000
    print('step2 use ' + str(t))

    resp = {
        "code": 0
    }
    return HttpResponse(json.dumps(resp), content_type="application/json")

import datetime
# 新增QQ响应时间
@csrf_exempt
def upload_v2(request):
    print('index upload')
    file_obj = request.FILES.get('file', None)
    print(file_obj.name)
    print(file_obj.size)

    info.objects.all().delete()
    t1 = time.time()

    start_flag = 0
    qq_group = ''
    qq_date = ''
    qq_oper = ''
    qq_time = ''
    qq_no = ''
    qq_data = []
    tmp_line_list = []
    old_qq_no = ''
    for line in file_obj.readlines():
        line = str(line.decode('utf-8'))
        # line = line.replace('\n', '')
        line = line.replace('\r', '')
        line = line.replace('\n', '')

        if line.startswith('================================================================'):
            continue
        # print(line, end='\n')
        #if len(line) > 0:
        # 消息对象:清镇兴邦-运营服务
        if line.startswith('消息对象:'):
            qq_group = line.split(':')[1]
            start_flag = 1

            # print('qq_group = ' + qq_group)
            continue

        if start_flag == 2:
            # print(qq_group + ':' + qq_date + ':' + qq_oper + ':' + line)
            try:
                re.match(r'\d\d\d\d-\d\d-\d\d \d*:\d\d:\d\d ', line).span()
                # print(str(start_flag) + ':new:' + line)
                now_date = datetime.datetime.strptime(qq_date + ' ' + qq_time,"%Y-%m-%d %H:%M:%S")
                try:
                    sec_date = now_date - old_date
                except:
                    sec_date = now_date - now_date

                qq_data.append({
                    'group': qq_group
                    , 'date': qq_date
                    , 'time': qq_time
                    , 'oper': qq_oper
                    , 'qq_no': qq_no
                    , 'use_sec': sec_date.total_seconds()
                    , 'content': ' '.join(tmp_line_list)
                })
                if old_qq_no != qq_no:
                    old_qq_no = qq_no
                    old_date = datetime.datetime.strptime(qq_date + ' ' + qq_time,"%Y-%m-%d %H:%M:%S")
                tmp_line_list.clear()
                start_flag = 1
            except Exception as msg:
                # print(str(start_flag) + ':append:' + str(msg))
                tmp_line_list.append(line)
                continue
            # r = info(
            #     group=qq_group
            #     , date=qq_date
            #     , oper=qq_oper
            #     , content=line
            # )
            # try:
            #     r.save()
            # except:
            #     print(qq_group + ':' + qq_date + ':' + qq_oper + ':' + line)



        if start_flag == 1:
            # 2017-12-26 8:33:02 兴业金融云-服务台I(1275494344)
            try:
                re.match(r'\d\d\d\d-\d\d-\d\d \d*:\d\d:\d\d ', line).span()
                # print('ok')
                line_list = line.split(' ')
                qq_date = line_list[0]
                qq_time = line_list[1]
                try:
                    qq_no = line_list[-1].split('(')[1].split(')')[0]
                    qq_oper = line_list[-1].split('(')[0]
                except:
                    try:
                        qq_no = line_list[-1].split('<')[1].split('>')[0]
                        qq_oper = line_list[-1].split('<')[0]
                    except:
                        qq_no = ''
                        qq_oper = line_list[2]
                start_flag = 2
                continue
            except Exception as msg:

                # print(qq_group + ':' + qq_date + ':' + qq_oper + ':' + line + ':' + str(msg))
                if len(line) > 0:
                    print(str(start_flag) + ':' + line + ':' + str(msg))

                continue
            # print(line)


    # 用时计算
    t2 = time.time()
    t = (t2 - t1) * 1000
    print('step1 use ' + str(t))
    # 保存下发范围
    json_file_name = '/home/insp_ap/tools/qq/data.json'
    print(json_file_name)
    f_resp = open(json_file_name, 'w', encoding='utf-8')
    json.dump(qq_data, f_resp, ensure_ascii=False, indent=4)

    # 用时计算
    t3 = time.time()
    t = (t3 - t2) * 1000
    print('step2 use ' + str(t))

    resp = {
        "code": 0
    }
    return HttpResponse(json.dumps(resp), content_type="application/json")

def show(request):
    print('start index show')

    # 权限检查
    auth_data = {
        'request': request
        , 'net': False
        , 'login': True
        , 'perm': ''
    }
    resp_auth = main.auth(auth_data)
    if resp_auth.get('code') == False:
        return render(request, 'alarm/resp.html', {"message": resp_auth.get('msg')})

    req = {
        'title': 'show'
    }
    # print(req)
    return render(request, 'qq_data/show.html', req)

def myview_show(request):
    print('start index myview_show')

    # 权限检查
    auth_data = {
        'request': request
        , 'net': False
        , 'login': True
        , 'perm': ''
    }
    resp_auth = main.auth(auth_data)
    if resp_auth.get('code') == False:
        return render(request, 'alarm/resp.html', {"message": resp_auth.get('msg')})

    req = {
        'title': 'myview_show'
    }
    # print(req)
    return render(request, 'qq_data/myview_show.html', req)


def search_problem_show(request):
    req = {}
    return render(request, 'qq_data/search_problem_show.html', req)

def search_problem_score(request):
    print('index search_problem_score')
    start_date = datetime.datetime.now()
    end_date = datetime.datetime.now()
    for line in range(7):
        print(line)
        print(start_date.strftime("%Y-%m-%d"))
        start_date -= datetime.timedelta(days=1)
    req = {
        'start_date': start_date.strftime("%Y-%m-%d")
        , 'end_date': end_date.strftime("%Y-%m-%d")
    }
    print(req)
    return render(request, 'qq_data/search_problem_score.html', req)