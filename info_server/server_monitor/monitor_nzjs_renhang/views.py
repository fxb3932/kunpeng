from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt    #可post调用url
import json

# Create your views here.

def index(request):
    print('start index rota_day')

    req = {
        'title': '年终决算'
    }
    # print(req)
    return render(request, 'monitor_nzjs_renhang/index.html', req)

@csrf_exempt
def get_data(request):
    f = open("/home/insp_ap/devops/info_server/static/app/monitor_nzjs/ALL", encoding='utf-8')
    info = json.load(f)

    step_list = ['rjbz','check9202','tspcl','jtzzs','open9119','syjz','pcljs','phcl']

    all_num = 0
    suc_num = 0
    #    if ( _resp_code < 100 ) return '状态未知';
    #    if ( _resp_code === 100 ) return '未开始';
    #    if ( _resp_code === 200 ) return '成功';
    #    if ( _resp_code === 300 ) return '进行中';
    #    if ( _resp_code === 400 ) return '异常';
    for line in info:
        print(line)
        for step_line in step_list:
            if line.get(step_line) == 200: suc_num += 1
        all_num += 1

    print('合作行总数：' + str(all_num))
    all_step_num = all_num * 8
    print('总步骤数：' + str(all_step_num))
    print('已完成步骤数：' + str(suc_num))
    suc_per = suc_num / all_step_num
    print('已完成百分比：' + str(suc_per))

    # http://163.1.6.40:19096/monitor_nzjs_renhang/get_data
    # http://163.1.6.40:19092/monitor_nzjs_renhang/get_data
    data = {
        '汇总数据': {
            '已完成百分比': 0.40
            , '进行中百分比': 0.73
            , '失败百分比': 0.98
        }

        , 'aaa':[
            {'x': 1, 'y': 20}
            , {'x': 2, 'y': 40}
            , {'x': 3, 'y': 50}
            , {'x': 4, 'y': 30}
            , {'x': 5, 'y': 20}
        ]
        , 'bbb':[
            {'name': 'aaa', 'value': 0.30}
            , {'name': 'aaa', 'value': 0.30}
            , {'name': 'bbb', 'value': 0.50}
        ]
    }
    return HttpResponse(json.dumps(data), content_type="application/json")