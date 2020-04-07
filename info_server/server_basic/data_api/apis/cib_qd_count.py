from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt    #可post调用url
import json

from django.contrib.auth.models import User
import main
shell = main.Shell()

@csrf_exempt
def cib_qd_count(request):
    print('start api cib_qd_count')

    print(request.POST)

    api_pwd = '/home/insp_ap/inspect/src/switch/cib/count/cib_qd_info/api'

    # 每日交易量
    data1=[]
    resp = shell.runCmd('sh ' + api_pwd + '/trans_day_count.sh')

    for line in resp[1].decode('GBK').split('\n'):
        if len(line.split('|')) == 2:
            print(line.split('|'))
            data1.append({
                'x': line.split('|')[0]
                , 'y': line.split('|')[1]
            })

    # 昨日交易分布情况
    data2=[]
    resp = shell.runCmd('sh ' + api_pwd + '/trans_qdzl_group.sh')

    for line in resp[1].decode('GBK').split('\n'):
        if len(line.split('|')) == 2:
            print(line.split('|'))
            data2.append({
                'value': line.split('|')[0]
                , 'id': line.split('|')[1]
            })

    # 渠道每日交易情况
    shell.runCmd('sh ' + api_pwd + '/trans_day_group.sh')
    f = open(api_pwd + '/trans_day_group.json', encoding='gbk')
    list_qd_trans = json.load(f)

    print(list_qd_trans)


    # http://163.1.6.40:19092/data_api/cib_qd_count/
    # http://163.1.6.40:19096/data_api/cib_qd_count/
    data = {
        'code': 0
        , '每日交易量': data1
        , '昨日交易分布情况': data2
        , '渠道每日交易情况': list_qd_trans
    }
    return HttpResponse(json.dumps(data), content_type="application/json")