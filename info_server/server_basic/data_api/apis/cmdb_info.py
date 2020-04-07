from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt    #可post调用url
import json

from cmdb.models import c_config2, i_bank

from django.forms.models import model_to_dict

import main
shell = main.Shell()

@csrf_exempt
def cmdb_info(request):
    print('start index test')

    print(request.POST)

    # 参数处理
    comm_s_plat_id = request.POST.get('comm_s_plat_id')
    if comm_s_plat_id and len(comm_s_plat_id) > 0:
        info = c_config2.objects.filter(plat__plat_id=comm_s_plat_id)
    else: info = c_config2.objects.all()

    data = []
    for line in info:
        data.append({
            "plat__plat_id": line.plat.plat_id
            , "plat__plat_ver__name": line.plat.plat_ver.name
            , "bank__name": line.bank.name
            , "bank__name_ch": line.bank.name_ch
            , "app_server__user": line.app_server.user
            , "app_server__ip": line.app_server.ip
            , "app_server__port": line.app_server.port
        })
        print(line)

    comm_i_c_config_bank = []
    for line in i_bank.objects.all():
        comm_i_c_config_bank.append(model_to_dict(line, exclude=['id']))


    # 批量导入合作行数据
    # batch_save_bank()


    resp = {
        'code': 0
        , 'data': data
        , 'comm_i_c_config_bank': comm_i_c_config_bank

    }
    return HttpResponse(json.dumps(resp), content_type="application/json")

from cmdb.models import i_app_server
def batch_save_bank():
    print('data update')
    # 批量导入合作行数据
    resp = shell.runCmd('cat /home/insp_ap/inspect/src/switch/nzjs/show.ini')
    # for line in resp[1].decode('GBK').split('\n'):
    #     if len(line.split(':')) > 7:
    #         r = i_bank(
    #             yhdm=line.split(':')[6]
    #             , name=line.split(':')[1]
    #             , name_ch=line.split(':')[0]
    #         )
    #         try:
    #             r.save()
    #             print(line.split(':')[1] + ' save ok')
    #         except:
    #             print(line.split(':')[1] + ' save err')

    # for line in resp[1].decode('GBK').split('\n'):
    #     if len(line.split(':')) > 7:
    #         print(line)
    #         app_server = i_app_server(
    #             user=line.split(':')[2]
    #         )

from cmdb.models import i_app_server, i_agent_ver, c_config_v1, i_plat
import time
@csrf_exempt
def update(request, api):
    print('def update ' + api)

    # 导入IP信息表
    # http://163.1.6.40:19096/data_api/cmdb_info/i_app_server/
    if api == 'i_app_server' and 1 == 2:
        print('update ' + api)
        # 1_AIX
        # 2_SUSE
        # 3_CENTOS
        i_agent_ver_data = i_agent_ver.objects.all()
        # for line in i_agent_ver_data.all():
        #     print(str(line.id) + '_' + line.name)

        resp = shell.runCmd('cat /home/insp_ap/inspect/src/switch/nzjs/show.ini')
        for line in resp[1].decode('GBK').split('\n'):
            if len(line.split(':')) > 7:
                # print(line)
                # 黔西花都 0:QXHD 1:cib 2:AIX 3:163.7.84.1 4:XXX 5:52035 6:村镇 7:10066 8:v3plus 9:v3plus 10
                app_server = i_app_server(
                    user=line.split(':')[2]
                    , agent_ver=i_agent_ver.objects.get(id=1)
                    , app_ver=line.split(':')[9]
                    , ip=line.split(':')[4]
                    , port=line.split(':')[8]
                    , create_time=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
                    , update_time=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
                )

                print(app_server.__dict__)
                try:
                    app_server.save()
                    print(line.split(':')[4] + ' save ok')
                except:
                    print(line.split(':')[4] + ' save err')

    if api == 'config_v1_v2' :
        print('update ' + api)
        resp = shell.runCmd('cat /home/insp_ap/inspect/src/switch/nzjs/show_v2.ini')
        for line in resp[1].decode('GBK').split('\n'):
            if len(line.split(':')) > 7:
                # 黔西花都 0:QXHD 1:cib 2:AIX 3:163.7.84.1 4:XXX 5:52035 6:村镇 7:10066 8:v3plus 9:v3plus 10
                print(line)
                config_v1_v2 = c_config_v1(
                    plat=i_plat.objects.get(id=1)
                    , app_server=i_app_server.objects.get(ip=line.split(':')[4])
                    # , bank=
                    #, app_type
                    #, app_stat
                    #, app_mode
                    #, create_time
                    #, update_time
                )
                print(config_v1_v2.__dict__)


    resp = {
        "code": 0
    }
    return HttpResponse(json.dumps(resp), content_type="application/json")


