from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt  # 可post调用url
import json


# Create your views here.

def index(request):
    print('start index rota_day')

    req = {
        'title': '年终决算'
    }
    # print(req)
    return render(request, 'monitor_nzjs/index.html', req)

import sys
sys.path.append('../')
import main
shell = main.Shell()


@csrf_exempt
def get_data(request):
    f = open("/home/insp_ap/devops/info_server/static/app/monitor_nzjs/ALL", encoding='utf-8')
    info = json.load(f)

    step_list = ['rjbz', 'check9202', 'tspcl', 'jtzzs', 'open9119', 'syjz', 'pcljs', 'phcl']

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
    all_step_num = all_num * len(step_list)
    print('总步骤数：' + str(all_step_num))
    print('已完成步骤数：' + str(suc_num))
    suc_per = suc_num / all_step_num
    print('已完成百分比：' + str(suc_per))

    # 独立节点决算步骤进度
    dljd_data = {}
    for step_line in step_list:
        step_suc_num = 0
        for line in info:
            if line.get(step_line) == 200: step_suc_num += 1

        dljd_data = dict(dljd_data, **{
            step_line: step_suc_num / len(info) - 0.001
            , step_line + '-var': step_suc_num / len(info)
            , step_line + '-num-ok': step_suc_num
            , step_line + '-num-wait': len(info) - step_suc_num
        })

    print(dljd_data)

    # 排行榜
    phb_data = []
    oper_set = set()
    for line in info:
        oper_set.add(line.get('user'))

    print(oper_set)
    ok_oper_num = 0
    for line in oper_set:
        step_suc_num = 0
        step_all_num = 0
        for oper_line in info:
            if oper_line.get('user') == line :
                for step_line in step_list:
                    if oper_line.get(step_line) == 200: step_suc_num += 1
                    step_all_num += 1
        phb_data.append({
            'x': line
            ,'y': round(step_suc_num / step_all_num * 100, 1)
        })
        if step_suc_num / step_all_num == 1 : ok_oper_num += 1

    print(phb_data)
    phb_data.sort(key=lambda item: item.get('y'), reverse=False)

    # 已完成行数
    bank_suc_num = 0
    for line in info:
        if line.get('phcl') == 200 : bank_suc_num += 1

    # 分版本决算进度
    ver_data = {}
    ver_set = set()
    for line in info:
        ver_set.add(line.get('patch'))
    print(ver_set)

    for ver_line in ver_set:
        step_suc_num = 0
        step_all_num = 0
        for info_line in info:
            if info_line.get('patch') == ver_line:
                for step_line in step_list:
                    if info_line.get(step_line) == 200: step_suc_num += 1
                    step_all_num += 1
        ver_data = dict(ver_data, **{
            str(ver_line): step_suc_num / step_all_num - 0.001
            , str(ver_line) + '-var': step_suc_num / step_all_num
            # ver_line: step_suc_num / step_all_num - 0.001
            # , str(ver_line) + '-var': step_suc_num / step_all_num
        })

    print(ver_data)

    resp = shell.runCmd('sh ./server_monitor/monitor_nzjs/shell/get_usetime.sh')
    print('-----resp-----')
    print(resp[1].decode('GBK'))
    print('-----end------')
    useTimeList = []

    for line in resp[1].decode('GBK').split('\n'):
        if len(line.split('|')) == 3:
            print(line.split('|'))
            useTimeList.append({
                'bank_name': line.split('|')[0]
                , 'bank_step': line.split('|')[1]
                , 'bank_usetime': line.split('|')[2]
            })

    runStepList = []
    resp = shell.runCmd('sh ./server_monitor/monitor_nzjs/shell/get_runlist.sh')

    for line in resp[1].decode('GBK').split('\n'):
        if len(line.split('|')) == 2:
            print(line.split('|'))
            runStepList.append({
                'x': line.split('|')[0]
                , 'y': line.split('|')[1]
            })
    # http://163.1.6.40:19096/monitor_nzjs/get_data
    # http://163.1.6.40:19092/monitor_nzjs/get_data
    data = {
        '独立节点决算步骤进度': dljd_data
        , '操作人员倒序排行榜': {
            '总人数': len(oper_set)
            , '已完成': ok_oper_num
            , '排行榜':phb_data[0:10]
        }
        , '实时预警': {
            '总行数': len(info)
            , '已完成行数': bank_suc_num
        }
        , '年终决算总进度': {
            '已完成百分比': suc_per - 0.001
        }
        , '分版本决算进度': ver_data
        , '步骤耗时统计': useTimeList
        , '操作统计': runStepList
    }
    return HttpResponse(json.dumps(data), content_type="application/json")
