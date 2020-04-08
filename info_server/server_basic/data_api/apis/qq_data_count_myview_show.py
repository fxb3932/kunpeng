from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt  # 可post调用url
import json


import time
import datetime
from myview.models import Article
from django.db.models import Count
from rjxf_server.models import flow

@csrf_exempt
def qq_data_count_myview_show(request):
    print('start index qq_data_count_myview_show')
    t1 = time.time()

    start_date = datetime.datetime.strptime(request.POST.get('start_date'),"%Y-%m-%d")
    end_date = datetime.datetime.strptime(request.POST.get('end_date'),"%Y-%m-%d")

    print('date : ' + start_date.strftime("%Y-%m-%d") + ' ~ ' + end_date.strftime("%Y-%m-%d"))

    tmp = list(Article.objects.all()
               .extra(select={"CreateTime": "date_format(date,'%%Y-%%m-%%d')"})
               .values('CreateTime')
               .annotate(count=Count('date')))

    list_date = []
    tmp_date = start_date
    while tmp_date <= end_date:
        list_date.append(tmp_date.strftime("%Y-%m-%d"))
        print(list_date)
        tmp_date += datetime.timedelta(days=1)

    data = []
    for line in tmp:
        print(line.get('CreateTime'))
        if line.get('CreateTime') in list_date:
            data.append(line)



    # data.sort(key=lambda item: item.get('CreateTime'), reverse=False)
    # rjxf_type = 0 普通版本  1 紧急版本
    tmp_0 = list(flow.objects.filter(rjxf_type=0)
               .extra(select={"CreateTime": "date_format(update_date,'%%Y-%%m-%%d')"})
               .values('CreateTime')
               .annotate(count=Count('update_date')))

    tmp_1 = list(flow.objects.filter(rjxf_type=1)
               .extra(select={"CreateTime": "date_format(update_date,'%%Y-%%m-%%d')"})
               .values('CreateTime')
               .annotate(count=Count('update_date')))

    data2 = []
    for line in list_date:
        print(line)
        n = 0
        for line_sub in tmp_0:
            if line_sub.get('CreateTime') == line:
                n = line_sub.get('count')
        data2.append({
            "CreateTime": line
            , 'count': n
        })

    data3 = []
    for line in list_date:
        print(line)
        n = 0
        for line_sub in tmp_1:
            if line_sub.get('CreateTime') == line:
                n = line_sub.get('count')
        data3.append({
            "CreateTime": line
            , 'count': n
        })

    # for line in tmp_0:
    #     if line.get('CreateTime') in list_date:
    #         data2.append(line)
    #
    # data3 = []
    # for line in tmp_1:
    #     if line.get('CreateTime') in list_date:
    #         data3.append(line)


    resp = {
        'code': 0
        , 'data': data
        , 'data2': data2
        , 'data3': data3
    }
    return HttpResponse(json.dumps(resp), content_type="application/json")
