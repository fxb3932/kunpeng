from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.models import Group
from myview.models import Article
import requests
import main
def index(request):
    print('index myview home')

    # 权限检查
    # resp_auth = main.auth(request, True, False, '')
    # if resp_auth[0] == False:
    #     return render(request, 'alarm/resp.html', {"message": resp_auth[1]})
    auth_data = {
        'request': request
        , 'net': False
        , 'login': False
        , 'perm': ''
    }
    resp_auth = main.auth(auth_data)
    if resp_auth.get('code') == False:
        return render(request, 'alarm/resp.html', {"message": resp_auth.get('msg')})

    user = request.user

    # 调用数据中台API
    res = requests.post(
        url='http://' + request.META.get('HTTP_HOST') + '/' + 'data_api/oper/'
        , data={"comm_i_user_first_name": user.first_name}
    )
    resp = json.loads(res.text)

    user_data = {}
    for line in resp.get('data'):
        user_data = line



    if user_data.get('is_authenticated') == True:
        user_id = user_data.get('first_name')
    else:
        user_id = '未登陆'
    req = {
        "user_id": user_id
        , "score": user_data.get('score')
    }

    for line in user_data.get('group_data'):
        if line.get('name') == '应用人员':
            return render(request, 'myview/index.html', req)
    return render(request, 'myview/index2.html', req)

def console(request):
    return render(request, 'home/console.html')

import time
import json
from django.db.models import Count
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def add_connect(request):
    # data = Article.objects.all()
    # print(data)
    # print(data.query)
    # print(data.count())


    # print(
    #     Article.objects.all()
    #         .extra(select={"CreateTime": "date_format(date,'%%Y%%m%%d %%H')"})
    #         .values('CreateTime')
    #         .annotate(count=Count('date'))
    #         # .values('CreateTime', 'count')
    #         .query
    # )



    # r = Article(
    #     date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    #     , user = 'FXB'
    #     , html_id = 'home'
    #     , html_title = '兴业数金鲲鹏管理平台'
    #     , browser_name = 'Google Chrome'
    #     , connect_type = '1'
    # )
    # print(r)
    # r.save()
    return HttpResponse(json.dumps({"msg": 'OK'}), content_type="application/json")

@csrf_exempt
def get_connect_group_by(request):
    print('run get_connect_group_by')
    # print(
    #     #Article.objects.filter({'date': '2019-07-16'})
    #     Article.objects.all()
    #         .extra(select={"CreateTime": "date_format(date,'%%Y%%m%%d %%H')"})
    #         .values('CreateTime')
    #         .annotate(count=Count('date'))
    #         # .values('CreateTime', 'count')
    #         .query
    # )
    s_date = time.strftime("%Y-%m-%d", time.localtime())
    data = list(Article.objects.filter(**{'date__contains': s_date})
            .extra(select={"CreateTime": "date_format(date,'%%H:00')"})
            .values('CreateTime')
            .annotate(count=Count('date')))
    print(data)
    return HttpResponse(json.dumps(data), content_type="application/json")

def login_index(request):
    return render(request, 'user/login.html')

# auth主认证模块
from django.contrib.auth.models import auth
#对应数据库，可以创建添加记录
from django.contrib.auth.models import User

@csrf_exempt
def login_in(request):
    print(request)
    print(request.GET.get('username'))
    print(request.GET.get('password'))
    print(request.user)
    user = auth.authenticate(username=request.GET.get('username'), password=request.GET.get('password'))
    if user is not None:
        auth.login(request, user)
        resp_code = 0
        resp_msg = '登入成功'
    else:
        resp_code = 1
        resp_msg = '用户不存在或用户密码不对哟'


    data = {
        "code": resp_code
        , "msg": resp_msg
        , "data": {
            "access_token": "c262e61cd13ad99fc650e6908c7e5e65b63d2f32185ecfed6b801ee3fbdd5c0a"
        }
    }
    return HttpResponse(json.dumps(data), content_type="application/json")

# from django.contrib.auth import logout
from django.contrib.auth import authenticate, login, logout

def user_logout(request):
    logout(request)
    return render(request, 'alarm/resp.html', {"message": "已登出"})

def register_index(request):
    return render(request, 'user/register.html')

@csrf_exempt
def test_resp(request):
    data = {
        'a': 111
        , 'b': 222
    }
    user = request.user
    if user.has_perm('rjxf_server.change_file_dir') == True:
        print('have perm')
        # user.user_permissions.add('rjxf_server.change_file_dir')
    else:
        print('no have perm')
    return HttpResponse(json.dumps(data), content_type="application/json")