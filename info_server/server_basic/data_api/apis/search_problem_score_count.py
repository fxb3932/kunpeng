from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt  # 可post调用url
import json
from main import connect_mysql

import requests
from cmdb.models import action, action_type, action_app_type
from django.db.models import Max,Avg,F,Q,Min,Count,Sum
import datetime
from django.forms.models import model_to_dict

@csrf_exempt
def search_problem_score_count(request):
    print('start index search_problem_score_count')

    # 获取日期列表
    start_date = datetime.datetime.strptime(request.POST.get('start_date'), "%Y-%m-%d")
    end_date = datetime.datetime.strptime(request.POST.get('end_date'), "%Y-%m-%d")
    end_date += datetime.timedelta(days=1)

    list_date = []
    tmp_date = start_date
    while tmp_date < end_date:
        list_date.append(tmp_date.strftime("%Y-%m-%d"))
        print(list_date)
        tmp_date += datetime.timedelta(days=1)

    print('start_date = ' + str(start_date))
    print('end_date = ' + str(end_date))
    # 调用数据中台API
    res = requests.post(
        url='http://' + request.META.get('HTTP_HOST') + '/' + 'data_api/oper/'
        , data={}
    )
    resp_oper = json.loads(res.text)

    data1 = {}
    list_first_name = []

    for line in resp_oper.get('data'):
        list_first_name.append({
            'first_name': line.get('first_name')
            # , 'score': line.get('score')
        })


    # {
    #     name: '解答',
    #     type: 'bar',
    #     stack: '总量',
    #     itemStyle: {normal: {label: {show: true, position: 'insideLeft'}, color: myColor[0]}},
    # // data: [320, 302, 301, 334, 390, 330, 320]
    # data: data.oper_all_sum.map(function(item, i)
    # {
    # return item.answer_sum;
    # })
    # },
    count_data = action.objects.filter(
        date__gte=start_date.strftime('%Y-%m-%d')
        , date__lt=end_date.strftime('%Y-%m-%d'))\
        .values('oper', 'action_type__code').annotate(score__sum=Sum('score'))


    type_data_query = action_type.objects.all()
    type_data = []

    for line in type_data_query:
        type_data.append(model_to_dict(line))

    count_data_all = []
    for line_name in list_first_name:
        for line_type in type_data:
            n = 0
            for line_data in count_data:
                #if line_data.get('oper') == line_name.get('first_name') and line_data.get('action_type__code') == line.code:
                if line_data.get('oper') == line_name.get('first_name') and line_data.get('action_type__code') == line_type.get('code'):
                    n += line_data.get('score__sum')
            count_data_all.append({
                'oper': line_name.get('first_name')
                , 'action_type__code': line_type.get('code')
                , 'score__sum': n
            })

    # {'id': 1, 'code': 'search', 'name': '搜索', 'score': 10, 'score_limit_day': 100}
    # print(type_data)
    # {'oper': '周勇', 'action_type__code': 'search', 'score__sum': 60}
    # print(count_data)

    tmp_list_first_name = []
    for line_name in list_first_name:
        n_sum = 0

        for line_data in count_data_all:
            if line_data.get('oper') == line_name.get('first_name'):
                n_sum += line_data.get('score__sum')

        # print(n_sum)
        tmp_list_first_name.append({
            'first_name': line_name.get('first_name')
            , 'score': n_sum
        })
    list_first_name = tmp_list_first_name


    list_first_name.sort(key=lambda item: item.get('score'), reverse=False)

    list_dict_series = []
    for line in action_type.objects.filter(~Q(code__in=['answer_auth_close', 'input_close', 'comments_close', 'answer_close'])):
        # print(line.__dict__)
        # 'id': 14, 'code': 'answer_auth_close', 'name': '解答认证被取消', 'score': -50, 'score_limit_day': 9999
        series_data = []
        for line_name in list_first_name:
            # count_data = action.objects.filter(
            #     oper=line_name
            #     , app_type=action_app_type.objects.get(code='search_problem')
            #     , action_type=action_type.objects.get(id=line.id)
            #     , date__gte='2020-04-01'
            #     , date__lte='2020-04-22'
            # ).aggregate(Sum('score'))
            n = 0
            n_close = 0
            for line_data in count_data_all:
                if line_data.get('oper') == line_name.get('first_name') and line_data.get('action_type__code') == line.code:
                    n = line_data.get('score__sum')

                    if line.code == 'comments':
                        for line_close_data in count_data_all:
                            if line_close_data.get('oper') == line_name.get('first_name') and line_close_data.get('action_type__code') == 'comments_close':
                                n_close += line_close_data.get('score__sum')
                    if line.code == 'answer_auth':
                        for line_close_data in count_data_all:
                            if line_close_data.get('oper') == line_name.get('first_name') and line_close_data.get('action_type__code') == 'answer_auth_close':
                                n_close += line_close_data.get('score__sum')
                    if line.code == 'input':
                        for line_close_data in count_data_all:
                            if line_close_data.get('oper') == line_name.get('first_name') and line_close_data.get('action_type__code') == 'input_close':
                                n_close += line_close_data.get('score__sum')
                    if line.code == 'answer':
                        for line_close_data in count_data_all:
                            if line_close_data.get('oper') == line_name.get('first_name') and line_close_data.get('action_type__code') == 'answer_close':
                                n_close += line_close_data.get('score__sum')
                    n += n_close
            series_data.append(n)
        list_dict_series.append({
            'name': line.name
            , 'type': 'bar'
            , 'stack': '总量'
            # , 'itemStyle': {'normal': {'label': {'show': -1, 'position': 'insideLeft'}, 'color': '#1089E7'}}
            , 'data': series_data
        })

    data1 = {
        'list_first_name': list_first_name
        , 'list_dict_series': list_dict_series
    }


    # count_data = action.objects.filter(
    #     app_type=action_app_type.objects.get(code='search_problem')
    #     , action_type=action_type.objects.get(code='search')
    #     , date__gte='2020-04-01'
    #     , date__lte='2020-04-22'
    # ).annotate(oper=Count('oper')).query
    # count_data = action.objects.all().values('oper', 'action_type__code').annotate(score__sum=Sum('score'))
    # count_data = action.objects.raw('''
    # select * from search_problem_action
    # ''')

    # .aggregate(Sum('score'))

    # print(count_data)
    # for line in count_data:
    #     print(line)
    # 汇总数据
    data2 = {}
    # 总积分数
    n = 0
    for line in resp_oper.get('data'):
        n += line.get('score')
    data2 = dict(data2, **{'val_score_all': n})
    # 今日增长量
    day_date = datetime.datetime.now()

    count_data = action.objects.filter(
        date__gte=day_date.strftime('%Y-%m-%d')).aggregate(Sum('score'))
    data2 = dict(data2, **{'var_score_day': count_data.get('score__sum')})

    # 按日统计积分获取量
    count_data = list(action.objects.filter(
        date__gte=start_date.strftime('%Y-%m-%d')
        , date__lt=end_date.strftime('%Y-%m-%d'))
        .extra(select={"DATE": "date_format(date,'%%Y-%%m-%%d')"})
        .values('DATE').annotate(score__sum=Sum('score')))

    data3 = []
    for line in list_date:
        n = 0
        for line_data in count_data:
            if line_data.get('DATE') == line:
                n = line_data.get('score__sum')

        data3.append({
            'DATE': line
            , 'score__sum': n
        })

    resp = {
        'code': 0
        , 'list_date': list_date
        , 'data1': data1
        , 'data2': data2
        , 'data3': data3
    }
    return HttpResponse(json.dumps(resp), content_type="application/json")
