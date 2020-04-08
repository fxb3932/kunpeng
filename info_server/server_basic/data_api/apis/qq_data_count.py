from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt  # 可post调用url
import json

# import sys
# sys.path.append('server_aiops')

from django.forms.models import model_to_dict

import time
from django.db.models import Q
import datetime
import requests
from cmdb.models import *




@csrf_exempt
def qq_data_count(request):
    print('start index qq_data_count')
    t1 = time.time()

    json_file_name = '/home/insp_ap/tools/qq/data.json'

    start_date = datetime.datetime.strptime(request.POST.get('start_date'),"%Y-%m-%d")
    end_date = datetime.datetime.strptime(request.POST.get('end_date'),"%Y-%m-%d")

    print('date : ' + start_date.strftime("%Y-%m-%d") + ' ~ ' + end_date.strftime("%Y-%m-%d"))

    if start_date > end_date:
        print('start > end')
    else:
        print('start < end')



    with open(json_file_name, "r", encoding='utf-8') as f:
        f_json = json.load(f)

    # 用时计算
    t2 = time.time()
    t = (t2 - t1) * 1000
    t1 = t2
    print('step1 use ' + str(t))

    # qq_data.append({
    #     'group': qq_group
    #     , 'date': qq_date
    #     , 'time'
    #     , 'oper': qq_oper
    #     , 'qq_no': qq_no
    #     , 'content': line
    # })

    list_date = []
    tmp_date = start_date


    while tmp_date <= end_date:
        list_date.append(tmp_date.strftime("%Y-%m-%d"))
        print(list_date)
        tmp_date += datetime.timedelta(days=1)

    qq_data = []
    for line in f_json:
        # group date oper content
        # data_date = datetime.datetime.strptime(line.get('date'),"%Y-%m-%d")
        # if data_date >= start_date and data_date <= end_date:
        if line.get('date') in list_date:
            qq_data.append(line)

    # 用时计算
    t2 = time.time()
    t = (t2 - t1) * 1000
    t1 = t2
    print('step2 use ' + str(t))
    print(len(qq_data))



    print(list_date)

    # 用时计算
    t2 = time.time()
    t = (t2 - t1) * 1000
    t1 = t2
    print('step3 use ' + str(t))
    print(len(qq_data))

    # 按天统计
    count_date = []
    tmp_data = []
    for line in list_date:
        print(line)
        tmp_data.clear()
        for line_sub in qq_data:
            if line_sub.get('date') == line:
                tmp_data.append(line_sub)

        count_date.append({
            "date": line
            , "sum": len(tmp_data)
        })

    # 按行统计 qq_data
    set_bank = set()
    for line in qq_data:
        if '运营服务' in line.get('group'):
            set_bank.add(line.get('group'))

    print(set_bank)
    list_bank_count = []
    for line in set_bank:
        tmp_data.clear()
        for line_sub in qq_data:
            if line_sub.get('group') == line:
                tmp_data.append(line_sub)

        print(str(line) + ':' + str(len(tmp_data)))
        list_bank_count.append({
            "group": line.replace('运营服务', '').replace('-', '')
            , "sum": len(tmp_data)
        })

    list_bank_count.sort(key=lambda item: item.get('sum'), reverse=False)
    list_bank_count_all = list_bank_count
    list_bank_count2 = list_bank_count[:20]
    list_bank_count = list_bank_count[-10:]


    list_bank_big_count = []
    tmp_list = [
        '达州银行-运营服务'
        , 'V3+哈密商行-运营服务'
        , 'V3+库尔勒银行-运营服务'
        , '邯郸银行'
        , '雅安商行-运营服务'
        , '梅州客商-运营服务'
        , '振兴银行-运营服务'
        , '新安银行-运营服务'
    ]
    for line in tmp_list:
        tmp_data.clear()
        for line_sub in qq_data:
            if line_sub.get('group') == line:
                tmp_data.append(line_sub)

        list_bank_big_count.append({
            "group": line.replace('运营服务', '').replace('运营服', '').replace('-', '')
            , "sum": len(tmp_data)
        })

    list_bank_big_count.sort(key=lambda item: item.get('sum'), reverse=False)

    list_bank_cz_count = []
    tmp_list = [
        'V3+南阳村镇-运营服务'
        , 'V3+沂源博商-运营服务'
        , 'V3+桂林国民-运营服务'
        , 'V3+闵行上银-运营服务'
        , 'V3+内江兴隆-运营服务'
        , 'V3+遵义长征-运营服务'
        , 'V3+大洼恒丰-运营服务'
        , 'V3+贵安发展-运营服务'
        , 'V3+嘉定洪都-运营服务'
        , 'V3+天津华明-运营服务'
    ]
    for line in tmp_list:
        tmp_data.clear()
        for line_sub in qq_data:
            if line_sub.get('group') == line:
                tmp_data.append(line_sub)

        list_bank_cz_count.append({
            "group": line.replace('运营服务', '').replace('运营服', '').replace('-', '')
            , "sum": len(tmp_data)
        })

    list_bank_cz_count.sort(key=lambda item: item.get('sum'), reverse=False)

    # qq_data = []
    # for line in f_json:
    #     # group date oper content
    #     if str(line.get('date')).startswith('2020-02-23'):
    #         qq_data.append(line)
    #
    # qq_data.sort(key=lambda item: item.get('time'), reverse=True)

    print(len(qq_data))

    # 调用数据中台API
    res = requests.post(
        url='http://' + request.META.get('HTTP_HOST') + '/' + 'data_api/oper/'
        , data={}
    )
    resp = json.loads(res.text)

    # bar_left3
    list_oper_count = []
    list_oper_count_all = []
    list_oper_count_HX = []
    list_oper_count_JG = []
    list_oper_count_GL = []
    list_oper_count_KF = []
    list_oper_count_max = 0
    for line_group in resp.get('comm_i_user_group'):
        if line_group.get('code') == 'HX':
            list_oper_count_HX = get_oper_info(qq_data, resp, line_group.get('code'), line_group.get('name'), list_oper_count_max)
            list_oper_count_max = list_oper_count_HX.get('list_oper_count_max')
        if line_group.get('code') == 'JG':
            list_oper_count_JG = get_oper_info(qq_data, resp, line_group.get('code'), line_group.get('name'), list_oper_count_max)
            list_oper_count_max = list_oper_count_JG.get('list_oper_count_max')
        if line_group.get('code') == 'GL':
            list_oper_count_GL = get_oper_info(qq_data, resp, line_group.get('code'), line_group.get('name'), list_oper_count_max)
            list_oper_count_max = list_oper_count_GL.get('list_oper_count_max')
        if line_group.get('code') == 'KF':
            list_oper_count_KF = get_oper_info(qq_data, resp, line_group.get('code'), line_group.get('name'), list_oper_count_max)
            # list_oper_count_max = list_oper_count_KF.get('list_oper_count_max')

    tmp_data.clear()
    bar_left3_series = []
    set_group_count_oper = set()

    for line in resp.get('comm_i_user_group'):
        tmp_data.append(line.get('name'))

        # 将分组人员名单存为数组
        set_group_count_oper.clear()
        for line_1 in resp.get('data'):
            if line_1.get('bc_group_code') == line.get('code'):
                set_group_count_oper.add(line_1.get('bc_qq_no'))

        i = 0
        for line_2 in qq_data:
            if line_2.get('qq_no') in set_group_count_oper:
                i += 1

        bar_left3_series.append({
            "name": line.get('name')
            , "type": 'bar'
            , 'markPoint': {
                'data': [
                    {'type': 'max', 'name': '最大值'}
                    , {'type': 'min', 'name': '最小值'}
                ]
            }
            , 'markLine': {'data': [{'type': 'average', 'name': '平均值'}]}
            , 'data': []
        })

    bar_left3_legend = {
        "data": tmp_data
    }

    #     series: [
    #         {
    #             name: 'KPI',
    #             type: 'bar',
    #         // data: [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3],
    #                  data: data.map(function(item, i)
    #     {
    #     return item.sum;
    #     }),
    #     markPoint: {
    #         data: [
    #     {type: 'max', name: '最大值'},
    #     {type: 'min', name: '最小值'}
    #
    # ]
    # },
    # markLine: {
    #     data: [{type: 'average', name: '平均值'}]
    # }
    # }
    # ]


    list_group_count = []
    for line in resp.get('comm_i_user_group'):
        if line.get('code') in ['HX', 'JG', 'GL', 'KF']:
            # 将分组人员名单存为数组
            set_group_count_oper.clear()
            for line_1 in resp.get('data'):
                if line_1.get('bc_group_code') == line.get('code'):
                    set_group_count_oper.add(line_1.get('bc_qq_no'))

            i = 0
            for line_2 in qq_data:
                if line_2.get('qq_no') in set_group_count_oper:
                    i += 1

            list_group_count.append({
                'name': line.get('name')
                , 'sum': i
            })

    # 用时计算
    t2 = time.time()
    t = (t2 - t1) * 1000
    t1 = t2
    print('step3 use ' + str(t))

    use_sec_count = 0



    # # 按天统计
    # tmp_data = []
    # tmp_data_2 = []
    # for line_user in resp.get('data'):
    #     if line_user.get('bc_qq_no') != '':
    #         count_date_2 = []
    #         tmp_data_3 = []
    #         for line_date in list_date:
    #             tmp_data.clear()
    #             use_time_count = 0
    #             for line_sub in qq_data:
    #                 if line_sub.get('date') == line_date \
    #                         and line_sub.get('qq_no') == line_user.get('bc_qq_no') \
    #                         and line_sub.get('use_sec') < 7200:
    #                     tmp_data.append(line_sub)
    #                     use_time_count += line_sub.get('use_sec')
    #
    #
    #             count_date_2.append({
    #                 "date": line_date
    #                 , "sum": len(tmp_data)
    #                 , 'use_time_count': use_time_count
    #             })
    #             try:
    #                 n = int(use_time_count/len(tmp_data))
    #             except:
    #                 n = 0
    #             tmp_data_3.append(n)
    #         tmp_data_2.append({
    #             'user': line_user.get('first_name')
    #             , 'qq_no': line_user.get('bc_qq_no')
    #             , 'data_list': tmp_data_3
    #             , 'data': count_date_2
    #
    #         })


    # print(count_date_2)
    # for line in count_date_2:
    #     print(line)

    # bar_6_data = []
    # bar_6_x = list_date
    # for line_group in resp.get('comm_i_user_group'):
    #     print(line_group)
    #     data_2 = []
    #
    #     for line_user in resp.get('data'):
    #         if line_user.get('bc_group_code') == line_group.get('code'):
    #             data_3 = []
    #             for line_data in tmp_data_2:
    #                 if line_data.get('qq_no') == line_user.get('bc_qq_no'):
    #                     data_3 = line_data.get('data_list')
    #
    #             data_2.append({
    #                 'name': line_user.get('first_name')
    #                 , 'type': 'line'
    #                 , 'data': data_3
    #             })
    #
    #     bar_6_data.append(dict(line_group, **{
    #         'data': data_2
    #     }))
    #
    #
    # for line in bar_6_data:
    #     print(line)

    resp = {
        'code': 0
        , 'data': qq_data
        , 'list_date': list_date
        , 'count_date': count_date
        , 'list_bank_count': list_bank_count
        , 'list_bank_count2': list_bank_count2
        , 'list_bank_count_all': list_bank_count_all
        , 'list_bank_big_count': list_bank_big_count
        , 'list_bank_cz_count': list_bank_cz_count
        , 'list_oper_count': list_oper_count
        , 'list_oper_count_max': list_oper_count_max
        # , 'list_oper_count_max': 570
        , 'list_oper_count_HX': list_oper_count_HX
        , 'list_oper_count_JG': list_oper_count_JG
        , 'list_oper_count_GL': list_oper_count_GL
        , 'list_oper_count_KF': list_oper_count_KF
        , 'list_group_count': list_group_count
        # , 'bar_6_data': bar_6_data
        , 'bar_left3': {
            "legend": bar_left3_legend
            , "series": bar_left3_series
        }
    }
    return HttpResponse(json.dumps(resp), content_type="application/json")

def get_oper_info(qq_data, resp, code, name, list_oper_count_max):
    print('into get_oper_info code = ' + code + ' name = ' + name)
    list_oper_count = []
    tmp_data = []
    for line in resp.get('data') :
        if line.get('bc_qq_no') != '' and line.get('bc_group_code') == code:
            tmp_data.clear()
            for line_sub in qq_data:
                if line_sub.get('qq_no') == line.get('bc_qq_no'):
                    tmp_data.append(line_sub)

            list_oper_count.append({
                'first_name': line.get('first_name')
                , 'sum': len(tmp_data)
            })
            if list_oper_count_max < len(tmp_data):
                list_oper_count_max = len(tmp_data)
            print(list_oper_count)
    return {
        'code': code
        , 'name': name
        , 'data': list_oper_count
        , 'list_oper_count_max': list_oper_count_max
    }