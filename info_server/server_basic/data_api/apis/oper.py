from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt    #可post调用url
import json

from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from cmdb.models import *
import requests

@csrf_exempt
def oper(request):
    print('start api oper')

    print(request.POST)

    search_info_data = User.objects.all()

    # 通过用户名筛选
    comm_i_user_first_name = request.POST.get('comm_i_user_first_name')
    if comm_i_user_first_name != None and comm_i_user_first_name != '':
        search_info_data = search_info_data.filter(first_name=comm_i_user_first_name)

    comm_i_user_first_name = []
    for line in User.objects.all():
        comm_i_user_first_name.append(line.first_name)

    comm_i_user_group = []
    for line in i_user_group.objects.all():
        comm_i_user_group.append({
            "code": line.code
            , "name": line.name
        })


    # 积分基础数据提取
    res = requests.post(
        url='http://' + request.META.get('HTTP_HOST') + '/' + 'data_api/search_problem_score/'
        , data={}
    )
    resp_score = json.loads(res.text)

    data = []
    for line in search_info_data.all():
        group_data = []
        for line_group in Group.objects.filter(user=line):
            group_data.append({
                'id': line_group.id
                , 'name': line_group.name
                # , 'name': line_group.name
            })

        # list_user_info = user_info.objects.get(first_name=line.first_name)
        try:
            list_user_info = user_info.objects.get(first_name=line.first_name)
            bc_qq_code = list_user_info.qq_no
        except:
            bc_qq_code = ''

        try: bc_group_code = list_user_info.group.code
        except: bc_group_code = ''
        try: bc_group_name = list_user_info.group.name
        except: bc_group_name = ''

        # score 用户积分计算
        # db = pymysql.connect("localhost", "testuser", "test123", "TESTDB")

        score = 0
        score_data = {}
        for line_score in resp_score.get('data'):
            if line_score.get('first_name') == line.first_name:
                score_data = line_score

        score_data.setdefault('score_sum', 0)
        score_data.setdefault('data', [])

        data.append({
            'id': line.id
            , 'username': line.username
            , 'first_name': line.first_name

            , 'score': score_data.get('score_sum')
            , 'score_data': score_data.get('data')

            , 'bc_qq_no': bc_qq_code
            , 'bc_group_code': bc_group_code
            , 'bc_group_name': bc_group_name

            , 'last_login': str(line.last_login)
            , 'is_active': line.is_active
            , 'is_anonymous': line.is_anonymous
            , 'is_authenticated': line.is_authenticated
            , 'is_staff': line.is_staff
            , 'is_superuser': line.is_superuser
            , 'group_data': group_data
        })



    resp = {
        "code": 0
        , "data": data
        , "comm_i_user_first_name": comm_i_user_first_name
        , "comm_i_user_group": comm_i_user_group
    }
    return HttpResponse(json.dumps(resp), content_type="application/json")


def oper2(request):
    print('start api oper')

    print(request.POST)


    data = []
    for line in User.objects.all():
        data.append({
            'id': line.id
            , 'username': line.username
            , 'first_name': line.first_name
            , 'last_login': str(line.last_login)
            , 'is_active': line.is_active
            , 'is_anonymous': line.is_anonymous
            , 'is_authenticated': line.is_authenticated
            , 'is_staff': line.is_staff
            , 'is_superuser': line.is_superuser
        })

    resp = {
        "code": 0
        , "data": data
    }
    return json.dumps(resp)