from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt  # 可post调用url
import json

# import sys
# sys.path.append('server_aiops')


from search_problem.models import info, action
from django.forms.models import model_to_dict
from django.db.models import Count

import requests
import time
import datetime

@csrf_exempt
def search_problem_count_v2(request):
    print('start index search_problem_count_v2')

    # 调用数据中台API
    res = requests.post(
        url='http://' + request.META.get('HTTP_HOST') + '/' + 'data_api/search_problem/'
        , data=dict(request.POST)
    )
    resp_info = json.loads(res.text)

    # 调用数据中台API
    res = requests.post(
        url='http://' + request.META.get('HTTP_HOST') + '/' + 'data_api/oper/'
        , data={}
    )
    resp_oper = json.loads(res.text)

    # 获取日期列表
    start_date = datetime.datetime.strptime(request.POST.get('start_date'),"%Y-%m-%d")
    end_date = datetime.datetime.strptime(request.POST.get('end_date'),"%Y-%m-%d")
    list_date = []
    tmp_date = start_date
    while tmp_date <= end_date:
        list_date.append(tmp_date.strftime("%Y-%m-%d"))
        print(list_date)
        tmp_date += datetime.timedelta(days=1)

    oper_all_sum = []
    for line in resp_oper.get('data'):
        n1 = n2 = n3 = 0

        if line.get('first_name') not in ['钟鸣']:
            for line_info in resp_info.get('data'):
                if line_info.get('answer_oper') == line.get('first_name'):
                    n1 += 1
                if line_info.get('input_oper') == line.get('first_name'):
                    n2 += 1

            for line_comments in resp_info.get('comments_data'):
                if line_comments.get('update_oper') == line.get('first_name'):
                    n3 += 1
            oper_all_sum.append({
                'first_name': line.get('first_name')
                , 'answer_sum': n1
                , 'input_sum': n2
                , 'comments_sum': n3
                , 'sum': n1 + n2 + n3
            })

    oper_all_sum.sort(key=lambda item: item.get('sum'), reverse=False)



    action_data = list(action.objects.filter(
        date__gte=request.POST.get('start_date')
        , date__lte=request.POST.get('end_date')
    )
                      .extra(select={"date": "date_format(date,'%%Y-%%m-%%d')"})
                      .values('date')
                      .annotate(count=Count('date')))

    trans_data = []
    # 使用情况
    for line_date in list_date:
        print(line_date)
        n1 = n2 = n3 = n4 = 0
        for line_info in resp_info.get('data'):
            if line_date in line_info.get('input_date'):
                print(line_info)
                n1 += 1
            if line_date in line_info.get('answer_date'):
                print(line_info)
                n2 += 1
            if line_date in line_info.get('update_date'):
                print(line_info)
                n3 += 1
        for line_action in action_data:
            if line_date == line_action.get('date'):
                #if line_action.type_id == 1:
                n4 = line_action.get('count')

        trans_data.append({
            'date': line_date
            , 'input_sum': n1
            , 'answer_sum': n2
            , 'update_sum': n3
            , 'search_sum': n4
        })


    print('------')

    # for line in info.objects.all():
    #     if line.update_date == None:
    #         r = info.objects.get(id=line.id)
    #         r.update_date=r.input_date
    #         r.save()
    #         print(line)


    resp = {
        'code': 0
        # , 'resp_info': resp_info
        # , 'resp_oper': resp_oper
        , 'list_date': list_date
        , 'oper_all_sum': oper_all_sum
        , 'trans_data': trans_data
        , 'action_data': action_data
    }
    return HttpResponse(json.dumps(resp), content_type="application/json")
