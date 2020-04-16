from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt  # 可post调用url
import json

# Create your views here.
import main


def index(request):
    print('start index search_problem')

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

    req = {
        'title': 'rota_day'
    }
    # print(req)
    return render(request, 'search_problem/index.html', req)


import requests


# 我要提问 ImageField
def new(request):
    print('index new')
    type = request.GET.get('type')
    print('type = [' + str(type) + ']')

    # 权限检查
    auth_data = {
        'request': request
        , 'net': False
        , 'login': True
        , 'debug': False
        , 'perm': 'rjxf_server.view_flow'
    }


    resp_auth = main.auth(auth_data)
    # print('user : ' + request.user.first_name)
    if resp_auth.get('code') == False: return render(request, 'alarm/resp.html', {"message": resp_auth.get('msg')})

    t1 = time.time()

    # 调用数据中台API
    # 取人员名单
    res = requests.post(
        url='http://' + request.META.get('HTTP_HOST') + '/' + 'data_api/oper/'
        , data={}
    )
    resp = json.loads(res.text)
    t2 = time.time()
    t = (t2 - t1) * 1000
    print('oper use ' + str(t))

    # 取合作行名 data_api/cib_qd_count/
    res2 = requests.post(
        url='http://' + request.META.get('HTTP_HOST') + '/' + 'data_api/cmdb_info/'
        , data={"comm_s_plat_id": "cib"}
    )
    resp2 = json.loads(res2.text)

    t3 = time.time()
    t = (t3 - t2) * 1000
    print('cmdb_info use ' + str(t))

    # 调用数据中台API
    res3 = requests.post(
        url='http://' + request.META.get('HTTP_HOST') + '/' + 'data_api/search_problem/'
        , data={"comm_i_info_stat": 0}
    )
    resp3 = json.loads(res3.text)

    t4 = time.time()
    t = (t4 - t3) * 1000
    print('search_problem use ' + str(t))

    req = {
        'title': '小鲲知道'
        , 'oper': resp.get('data')
        , 'bank_info': resp2.get('comm_i_c_config_bank')
        , 'comm_i_info_channel': resp3.get('comm_i_info_channel')
        , 'comm_i_info_type': resp3.get('comm_i_info_type')
        , 'type': type
    }
    print('ok')
    return render(request, 'search_problem/new.html', req)


import os
import time


@csrf_exempt
def new_text_upload(request):
    file_pwd = os.getcwd() + '/static/app/search_problem/tupian/'
    file_obj = request.FILES.get('file', None)
    s_date = time.strftime('%Y-%m-%d-%H:%M:%S', time.localtime())

    print(file_pwd)
    print(file_obj.name)
    print(file_obj.size)

    file_name = s_date + '-' + file_obj.name
    with open(file_pwd + file_name, 'wb') as f:
        for line in file_obj.chunks():
            f.write(line)
        message = '上传[' + file_name + ']文件成功，大小[' + str(file_obj.size) + ']'
        code = 0
        f.close()

    resp = {
        "code": code
        , "msg": message
        , "data": {
            "src": "/static/app/search_problem/tupian/" + file_name
            , "class": "layui-upload-img"
            # , "title": "building.png"
        }
    }
    return HttpResponse(json.dumps(resp), content_type="application/json")

@csrf_exempt
def upload_file(request):

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
        resp = resp_auth
        return HttpResponse(json.dumps(resp), content_type="application/json")

    file_pwd = os.getcwd() + '/static/app/search_problem/file/'
    file_obj = request.FILES.get('file', None)
    s_date = time.strftime('%Y-%m-%d-%H:%M:%S', time.localtime())

    print(file_pwd)
    print(file_obj.name)
    print(file_obj.size)

    file_name = s_date + '-' + file_obj.name
    with open(file_pwd + file_name, 'wb') as f:
        for line in file_obj.chunks():
            f.write(line)
        message = '上传[' + file_name + ']文件成功，大小[' + str(file_obj.size) + ']'
        code = 0
        f.close()

    resp = {
        "code": code
        , "msg": message
        , "data": {
            "file_name": file_obj.name
            , "src": "/static/app/search_problem/file/" + file_name
            , "class": "layui-upload-img"
            # , "title": "building.png"
        }
    }
    # resp = {
    #     "code": 0
    #     , "msg": ""
    # }
    return HttpResponse(json.dumps(resp), content_type="application/json")

from .models import info
from bs4 import BeautifulSoup


@csrf_exempt
def new_submit(request):
    print('index new_submit')
    input_data = json.loads(request.POST.get('input_data'))
    fwb_data = request.POST.get('fwb_data')
    fwb_text_answer = request.POST.get('fwb_text_answer')
    user = request.user



    print(input_data)
    print(fwb_data)

    if request.POST.get('type') == 'input':
        stat = 1
    else:
        stat = 0

    print('type = [' + request.POST.get('type') + ']')

    print(fwb_text_answer)
    if fwb_text_answer is None:
        fwb_text_answer = ''
    if input_data.get('comm_i_info_channel') is None:
        info__t_channel = None
    else:
        info__t_channel = info_channel.objects.get(code=input_data.get('comm_i_info_channel'))

    if input_data.get('comm_i_info_type') is None:
        info__t_type = None
    else:
        info__t_type = info_type.objects.get(code=input_data.get('comm_i_info_type'))

    problem_answer = BeautifulSoup(fwb_text_answer, 'html.parser')

    r = info(
        title=input_data.get('title')
        , trans_code=input_data.get('trans_code')
        , trans_err=input_data.get('trans_err')
        , problem_info=fwb_data
        , problem_answer=fwb_text_answer
        , problem_answer_txt=problem_answer.get_text()
        , input_oper=user.first_name
        , answer_oper = input_data.get('answer_oper')
        , bank_id=input_data.get('bank_id')
        , bank_oper=input_data.get('bank_oper')
        , problem_source=input_data.get('problem_source')
        , input_date=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        , update_date=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        , t_stat=info_stat.objects.get(stat_id=stat)
        , t_channel=info__t_channel
        , t_type=info__t_type
        , info_check_flag=0
        , info_check_update=0
        , count_search=0
        , count_chick=0
    )
    code = 0
    msg = ''

    try:
        r.save()
        code = 0
        msg = '感谢您对知识库的完善：）'

        # 操作记录
        a = action(
            type=action_type.objects.get(code=3)
            , text=str(r.id)
            , oper=request.user.first_name
            , date=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        )
        a.save()
    except Exception as msg_info:
        code = -1
        print(repr(msg_info))
        print(msg_info)
        print(msg_info.args[0])

        if msg_info.args[0] == 1406:
            msg = '录入失败了，答案的内容超出长度限制，入库失败了哟~~~'
        elif msg_info.args[0] == 1062:
            msg = '录入失败了，可能该标题已存在，无法重复入库~'
        else:
            msg = '录入失败了。。。<br>报错信息：' + str(msg_info)
            # msg = '录入失败了~' + str(msg_info)

    resp = {
        "code": code
        , "msg": msg
    }
    return HttpResponse(json.dumps(resp), content_type="application/json")


from bs4 import BeautifulSoup
from .models import info_stat
from .models import info_channel
from .models import info_type
from .models import action, action_type

# 小鲲度
def search(request):
    print('def search')
    t1 = time.time()

    problem_id = request.GET.get('keywords')
    print('problem_id = [' + problem_id + ']')

    # 操作记录
    a = action(
        type = action_type.objects.get(code=1)
        , text = problem_id
        , oper = request.user.first_name
        , date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    )
    a.save()

    # contains 区分大小写 icontains 不区分
    # Entity.objects.filter(Q(name_icontains='kris') | Q(address_icontains='beijing'))
    # 调用数据中台API
    res = requests.post(
        url='http://' + request.META.get('HTTP_HOST') + '/' + 'data_api/search_problem/'
        , data={'comm_i_search': problem_id}
    )
    resp = json.loads(res.text)


    print(resp)
    data = []
    for line in resp.get('data'):
        # 计数 会严重影响查询时间
        # print(line)
        # r = info.objects.get(id=line.get('id'))
        # r.count_search += 1
        # r.save()

        data.append(line)

    # data.sort(key=lambda item: item.get('id'), reverse=True)
    data.sort(key=lambda item: item.get('t_stat_id'), reverse=True)
    data.sort(key=lambda item: item.get('info_check_flag'), reverse=True)



    # 用时计算
    t2 = time.time()
    t3 = (t2 - t1) * 1000

    req = {
        'title': 'search'
        , 'data': data
        , 'len': len(data)
        , 'problem_id': problem_id
        , 'use_time': int(t3)
    }
    return render(request, 'search_problem/search.html', req)

def show(request, info_id):
    print('index show')
    print('info_id = [' + str(info_id) + ']')

    # 计数
    r = info.objects.get(id=info_id)
    r.count_chick += 1
    r.save()

    comments_data = []
    for line in info.objects.filter(id=info_id):
        data = line.__dict__
        data_stat_id = line.t_stat.stat_id
        for line_comments in line.t_comments.all():
            # comments_data.append(model_to_dict(line_comments, exclude=['update_date']))
            comments_data.append({
                "name": line_comments.name
                , "update_oper": line_comments.update_oper
                , "update_date": line_comments.update_date.strftime("%Y-%m-%d %H:%M:%S")
            })

        try:
            data_channel_id = line.t_channel.code
            data_type_id = line.t_type.code
        except:
            data_channel_id = 666
            data_type_id = 666


    print(data)

    channel_data = []
    for line in info_channel.objects.all():
        channel_data.append(line.__dict__)

    type_data = []
    for line in info_type.objects.all():
        type_data.append(line.__dict__)

    # for line in
    # info_comments

    # 调用数据中台API
    res = requests.post(
        url='http://' + request.META.get('HTTP_HOST') + '/' + 'data_api/oper/'
        , data={"comm_i_user_first_name": request.user.first_name}
    )
    resp = json.loads(res.text)

    user_data = {}
    for line in resp.get('data'):
        user_data = line
    app_auth = 0
    for line in user_data.get('group_data'):
        if line.get('name') == '知识库管理员':
            app_auth = 1

    if data.get('info_check_flag') == 1:
        # 操作记录 认证解答被查看
        b = action(
            type=action_type.objects.get(code=8)
            , text=str(info_id)
            , oper=data.get('answer_oper')
            , date=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        )
        b.save()

        # 操作记录 认证录入被查看
        c = action(
            type=action_type.objects.get(code=9)
            , text=str(info_id)
            , oper=data.get('input_oper')
            , date=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        )
        c.save()

    # 操作记录
    a = action(
        type = action_type.objects.get(code=2)
        , text = str(info_id)
        , oper = request.user.first_name
        , date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    )
    a.save()




    resp = {
        "code": 0
        , "data": data
        , "type": 'new'
        , "stat": data_stat_id
        , "channel": channel_data
        , 'type_data': type_data
        , "data_channel_id": data_channel_id
        , "data_type_id": data_type_id
        , 'comments_data': comments_data
        , 'app_auth': app_auth
    }
    print(resp)
    return render(request, 'search_problem/show.html', resp)


@csrf_exempt
def show_submit(request, info_id):
    print('index new_submit')


    input_data = json.loads(request.POST.get('input_data'))
    fwb_data = request.POST.get('fwb_data')
    user = request.user

    print(input_data)
    print(fwb_data)

    print('type = [' + request.POST.get('type') + ']')
    r = info.objects.get(id=info_id)
    r.title = input_data.get('title')
    problem_answer = BeautifulSoup(fwb_data, 'html.parser')
    problem_answer_txt = problem_answer.get_text()
    r.problem_answer = fwb_data
    r.problem_answer_txt = problem_answer_txt
    if len(problem_answer_txt) > 1:
        r.t_stat = info_stat.objects.get(stat_id=1)
        if request.POST.get('type') == 'new':
            r.answer_oper = request.user.first_name
            r.answer_date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    else:
        r.t_stat = info_stat.objects.get(stat_id=0)
    r.update_date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    r.t_channel = info_channel.objects.get(code=input_data.get('channel'))
    r.t_type = info_type.objects.get(code=input_data.get('info_type'))
    r.info_check_update = 0

    if input_data.get('info_check_flag') == 'on':
        r.info_check_flag = 1
    else:
        r.info_check_flag = 0

    print(r)

    try:
        r.save()
        code = 0
        msg = '感谢您对知识库的完善：）'

        a = action(
            type=action_type.objects.get(code=4)
            , text=str(r.id)
            , oper=request.user.first_name
            , date=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        )
        a.save()
    except Exception as msg_info:
        code = -1
        print(repr(msg_info))
        print(msg_info)
        msg = '提交失败了。。。<br>报错信息：' + str(msg_info)
        # msg = '录入失败了，可能该标题已存在，无法重复入库~'

    resp = {
        "code": code
        , "msg": msg
    }

    return HttpResponse(json.dumps(resp), content_type="application/json")


def show_update(request, info_id):
    print('index show_update')

    # 权限检查
    auth_data = {
        'request': request
        , 'net': False
        , 'login': True
        , 'debug': False
        , 'perm': ''
        , 'perm_group': '知识库管理员'
    }
    resp_auth = main.auth(auth_data)
    print('user : ' + request.user.first_name)
    if resp_auth.get('code') == False: return render(request, 'alarm/resp.html', {"message": resp_auth.get('msg')})

    print('info_id = [' + str(info_id) + ']')
    for line in info.objects.filter(id=info_id):
        data = line.__dict__
        data_channel_id = line.t_channel.code
        data_type_id = line.t_type.code

    print(data)

    channel_data = []
    for line in info_channel.objects.all():
        channel_data.append(line.__dict__)

    type_data = []
    for line in info_type.objects.all():
        type_data.append(line.__dict__)

    comments_data = []
    for line in info.objects.filter(id=info_id):
        data = line.__dict__
        for line_comments in line.t_comments.all():
            comments_data.append({
                "name": line_comments.name
                , "update_oper": line_comments.update_oper
                , "update_date": line_comments.update_date.strftime("%Y-%m-%d %H:%M:%S")
            })

    comments_data.sort(key=lambda item: item.get('update_date'), reverse=True)

    resp = {
        "code": 0
        , "data": data
        , 'type': 'update'
        , "stat": 0
        , "channel": channel_data
        , 'type_data': type_data
        , "data_channel_id": data_channel_id
        , "data_type_id": data_type_id
        , "comments_data": comments_data
    }
    return render(request, 'search_problem/show.html', resp)


def submit_ok(request, info_id):
    print('index submit_ok')
    print('info_id = [' + str(info_id) + ']')

    resp = {
        "code": 0
        , "msg": "谢谢您对知识共享的支持，答案提交成功：）"
    }
    return render(request, 'search_problem/submit_ok.html', resp)


def list(request):
    print('index list')

    # 调用数据中台API
    res = requests.post(
        url='http://' + str(request.META.get('HTTP_HOST')) + '/' + 'data_api/search_problem/'
        , data={'comm_i_info_stat': 0}
    )
    resp = json.loads(res.text)

    # resp.get('data') = resp.get('data').sort(key=lambda item: item.get('count_sum'), reverse=True)


    resp = {
        "code": 0
        , "data": resp
    }
    return render(request, 'search_problem/list.html', resp)


@csrf_exempt
def get_table_data(request):
    print('index get_table_data')

    input_data = request.POST.get('input_data')

    try:
        data = json.loads(input_data)
    except:
        data = {"comm_i_info_stat": 0}

    # 调用数据中台API
    res = requests.post(
        url='http://' + request.META.get('HTTP_HOST') + '/' + 'data_api/search_problem/'
        , data=data
    )
    resp = json.loads(res.text)

    resp.get('data').sort(key=lambda item: item.get('count_sum'), reverse=True)

    # for line in info.objects.all():
    #     print(line.id)
    #     r = info.objects.get(id=line.id)
    #     r.info_check_update = 0
    #     r.save()

    resp = {
        "code": 0
        , "msg": ''
        , "count": 0
        , "data": resp.get('data')
    }
    return HttpResponse(json.dumps(resp), content_type="application/json")

from .models import info_comments
@csrf_exempt
def show_submit_comments(request, info_id):
    print('start show_submit_comments')

    fwb_data = request.POST.get('fwb_data')


    # name = models.CharField(max_length=64)
    # update_oper = models.CharField(max_length=64)
    # update_date = models.DateTimeField()
    r_comments = info_comments(
        name=fwb_data
        , update_oper=request.user.first_name
        , update_date=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    )


    code = -1
    msg = ''
    try:
        r_comments.save()
        print(r_comments.id)

        r = info.objects.get(id=info_id)
        r.t_comments.add(r_comments.id)
        r.update_date=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        r.info_check_update=1
        r.save()
        code = 0

        # 操作记录
        a = action(
            type=action_type.objects.get(code=4)
            , text=str(r.id)
            , oper=request.user.first_name
            , date=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        )
        a.save()
    except Exception as msg_info:
        r_comments.delete()
        msg = str(msg_info)

    resp = {
        "code": code
        , "msg": msg
    }
    return HttpResponse(json.dumps(resp), content_type="application/json")

def report(request, info_id):
    print('index submit_ok')
    print('info_id = [' + str(info_id) + ']')

    resp = {
        "code": 0
        , "msg": "谢谢您对知识共享的支持，答案提交成功：）"
    }
    return render(request, 'search_problem/report.html', resp)