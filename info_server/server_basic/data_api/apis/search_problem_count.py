from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt  # 可post调用url
import json

# import sys
# sys.path.append('server_aiops')


from search_problem.models import info
from search_problem.models import info_stat
from search_problem.models import info_channel
from search_problem.models import info_type
from search_problem.models import action
from django.forms.models import model_to_dict
from django.db.models import Count

import requests
import time


@csrf_exempt
def search_problem_count(request):
    print('start index search_problem_count')

    # 统计数据

    all_count = 0
    info_check_flag_count = 0
    t_stat__1 = 0
    for line in info.objects.all():
        all_count += 1
        print(line.info_check_flag)
        if line.info_check_flag == 1:
            info_check_flag_count += 1

        if line.t_stat.stat_id == 1:
            t_stat__1 += 1

    t_stat__1_suc = t_stat__1 / all_count - 0.001
    print(t_stat__1_suc)
    print(t_stat__1)
    print(all_count)
    print(1 / 2)

    # 调用数据中台API
    res = requests.post(
        url='http://' + request.META.get('HTTP_HOST') + '/' + 'data_api/search_problem/'
        , data={}
    )
    resp = json.loads(res.text)

    channel_type_data = []
    for line in resp.get('comm_i_info_channel'):
        channel_type_data.append(dict(line, **{
            "sum": len(info.objects.filter(t_channel__code=line.get('code')))
        }))
        print(line)

    info_type_data = []
    for line in resp.get('comm_i_info_type'):
        info_type_data.append(dict(line, **{
            "sum": len(info.objects.filter(t_type__code=line.get('code')))
        }))

    # 统计交易量
    s_date = time.strftime("%Y-%m-%d", time.localtime())
    trans_data = list(action.objects.filter(**{'date__contains': s_date})
                      .extra(select={"CreateTime": "date_format(date,'%%H:00')"})
                      .values('CreateTime')
                      .annotate(count=Count('date')))

    trans_sum = len(action.objects.filter(date__contains=s_date))

    trans_all_data = []
    tmp = list(info.objects.all()
               .extra(select={"CreateTime": "date_format(input_date,'%%m-%%d')"})
               .values('CreateTime')
               .annotate(count=Count('input_date')))

    for line in tmp:
        # print(line)
        n = len(action.objects.filter(date__contains=line.get('CreateTime')))
        # print(n)
        trans_all_data.append({
            "date": line.get('CreateTime')
            , "录入量": line.get('count')
            , "访问量": n
        })

    n_search = 0
    n_show = 0
    n_input = 0
    for line in action.objects.filter(date__contains=s_date):
        if line.oper == '李嘉欣' or line.oper == '王燕':
            if line.type.code == 1:
                n_search += 1
            if line.type.code == 2:
                n_show += 1
            if line.type.code == 3:
                n_input += 1
    kf_text = '今日搜索 ' + str(n_search) + ' 次，查看知识库 ' + str(n_show) + ' 次，录入问题 ' + str(n_input) + ' 个。'

    # 调用数据中台API
    res2 = requests.post(
        url='http://' + request.META.get('HTTP_HOST') + '/' + 'data_api/oper/'
        , data={}
    )
    resp_oper = json.loads(res2.text)

    oper_sum = []
    for line in resp_oper.get('data'):
        print(line)
        if line.get('first_name') not in ['费学彬','杨磊','钟鸣','吕伟钢']:
            oper_sum.append(dict(line, **{
                "sum": len(info.objects.filter(answer_oper=line.get('first_name')))
            }))

    oper_sum.sort(key=lambda item: item.get('sum'), reverse=True)




    resp = {
        'code': 0
        , '统计数据': {
            "总问题数": all_count
            , "知识卡片数量": info_check_flag_count
            , "方案提供率": t_stat__1_suc
            , "访问量": trans_sum
            , "客服专员情况说明": kf_text
        }
        , "渠道分类": channel_type_data
        , "类型分类": info_type_data
        , "交易情况": trans_data
        , "近期交易情况": trans_all_data
        , "人员录入量": oper_sum
    }
    return HttpResponse(json.dumps(resp), content_type="application/json")
