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

from search_problem.models import info, info_comments
from django.db.models import Max, Avg, F, Q, Min, Count, Sum


@csrf_exempt
def search_problem_count_v2(request):
    print('start index search_problem_count_v2')

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

    # 调用数据中台API
    res = requests.post(
        url='http://' + request.META.get('HTTP_HOST') + '/' + 'data_api/oper/'
        , data={}
    )
    resp_oper = json.loads(res.text)

    # info_data = info.objects.filter(
    #     input_date__gte=start_date.strftime('%Y-%m-%d')
    #     , input_date__lt=end_date.strftime('%Y-%m-%d'))
    info_data = info.objects.filter(~Q(t_close__code=999))

    info_input_data = info_data.filter(
        input_date__gte=start_date.strftime('%Y-%m-%d')
        , input_date__lt=end_date.strftime('%Y-%m-%d'))
    info_input_count = list(info_input_data
                            # .extra(select={OPER: 'input_oper'})
                            .annotate(OPER=F('input_oper'))
                            .values('OPER')
                            .annotate(count=Count('OPER')))
    info_answer_data = info_data.filter(
        answer_date__gte=start_date.strftime('%Y-%m-%d')
        , answer_date__lt=end_date.strftime('%Y-%m-%d'))
    info_answer_count = list(info_answer_data
                             .annotate(OPER=F('answer_oper'))
                             .values('OPER')
                             .annotate(count=Count('OPER')))
    info_comments_data = info_comments.objects.filter(
        update_date__gte=start_date.strftime('%Y-%m-%d')
        , update_date__lt=end_date.strftime('%Y-%m-%d'))
    info_comments_count = list(info_comments_data.annotate(OPER=F('update_oper')).values('OPER')
                               .annotate(count=Count('OPER')))


    # aaa = info.objects.filter(
    #     input_date__gte=start_date.strftime('%Y-%m-%d')
    #     , input_date__lt=end_date.strftime('%Y-%m-%d'))\
    #                         .extra(select={'OPER': 'aaa'}).values('OPER')
    #
    # for line in aaa:
    #     print(line.__dict__)
    print(info_input_count)
    print(info_answer_count)
    print(info_comments_count)


    list_first_name = []
    for line_oper in resp_oper.get('data'):
        n = 0
        for line_input in info_input_count:
            if line_input.get('OPER') == line_oper.get('first_name'):
                n += line_input.get('count')
        for line_answer in info_answer_count:
            if line_answer.get('OPER') == line_oper.get('first_name'):
                n += line_answer.get('count')
        for line_comments in info_comments_count:
            if line_comments.get('OPER') == line_oper.get('first_name'):
                n += line_comments.get('count')
        list_first_name.append({
            'first_name': line_oper.get('first_name')
            , 'sum': n
        })

    list_first_name.sort(key=lambda item: item.get('sum'), reverse=False)

    list_dict_series = []
    type_data = [
        {'name': '录入', 'data': info_input_count}
        , {'name': '解答', 'data': info_answer_count}
        , {'name': '评论', 'data': info_comments_count}
    ]
    for line in type_data:
        print(line)
        series_data = []
        for line_oper in list_first_name:
            count = 0
            for line_data in line.get('data'):
                if line_oper.get('first_name') == line_data.get('OPER'):
                    count += line_data.get('count')
            series_data.append(count)
        list_dict_series.append({
            'name': line.get('name')
            , 'type': 'bar'
            , 'stack': '总量'
            # , 'itemStyle': {'normal': {'label': {'show': -1, 'position': 'insideLeft'}, 'color': '#1089E7'}}
            , 'data': series_data
        })

    data1 = {
        'list_first_name': list_first_name
        , 'list_dict_series': list_dict_series
    }

    # 汇总数据
    # 总量 & 解答率
    time_id = time_begin()
    info_count = info_data.aggregate(Count('id')).get('id__count')

    answer_suc = info_data.filter(t_stat__stat_id=1).aggregate(Count('id')).get('id__count') / info_count
    answer_suc = float(answer_suc)


    data0 = {
        'card1_info_count': info_count
        , 'card1_answer_suc': round(answer_suc * 100, 1)
        , 'card2_input_count': info_input_data.aggregate(Count('id')).get('id__count')
        , 'card2_answer_count': info_answer_data.aggregate(Count('id')).get('id__count')
        , 'card2_comments_count': info_comments_data.aggregate(Count('id')).get('id__count')
    }
    print(data0)

    time_end(time_id, '汇总数据')

    index_2 = {}
    # data: ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月']
    # data: [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
    index_2_data = []
    for line in list_date:
        print(line)
        n = 0
        for line_input in info_input_data.extra(select={"DATE": "date_format(input_date,'%%Y-%%m-%%d')"})\
                .values('DATE').annotate(count=Count('id')):
            if line_input.get('DATE') == line:
                n += line_input.get('count')
        index_2_data.append({
            'date': line
            , 'count': n
        })
    index_2 = {
        'data': index_2_data
    }

    resp = {
        'code': 0
        , 'list_date': list_date
        , 'data0': data0
        , 'data1': data1
        , 'index_2': index_2
    }
    return HttpResponse(json.dumps(resp), content_type="application/json")

def time_begin():
    return time.time()

def time_end(t1, txt):
    t2 = time.time()
    t = (t2 - t1) * 1000
    print(txt + ' use time : ' + str(int(t)))
    return 0