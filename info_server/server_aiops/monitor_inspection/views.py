from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt  # 可post调用url
import json

# Create your views here.
import main
import os
import time

from cmdb.models import *
def index(request):
    print('start index monitor_inspection')
    # for line in i_plat.objects.all():
    #     print(line)


    # for  line in c_config_v1.objects.all():
    #     a=line
    #     print(line)
    #     print(line.app_mode)
    #     print(line.app_mode.name)
    #
    # rrr = c_config_v1.objects.get(id=5)
    # rrr.app_mode = i_app_mode.objects.get(code=2)

    # test=i_app_mode.objects.filter(code=2)
    # print(test)


    # a=c_config_v1(
    #     app_mode=i_app_mode.objects.filter(code=2)
    # )
    # a.save()



    for  line in c_config_v1.objects.all():
        a=line
        print(line)
        print(line.app_mode)
        print(line.app_mode.name)


    #
    # for line in c_config_v1.objects.filter():
    #     a = line
    #     print(line)
    #     print(line.app_mode)
    #
    # # i_plat.objects.all().delete()
    # a=i_plat(
    #     plat_id='WACZ',
    #     plat_name='aa'
    # )
    # a.save()








    # file_name="/home/insp_ap/tmp/yanghui/xunjian/result.txt"
    # print(os.getcwd())
    # with open(file_name, encoding='gbk') as file_obj:
    #     contents = file_obj.readlines()
    #     print(contents)
    #     for line in contents:
    #         line=line.strip("\n")
    #         #print(line)
    #         product_name=line.split(" ")[0]
    #         product_ch_name=line.split(" ")[1]
    #         product_version=line.split(" ")[2]
    #         product_team=line.split(" ")[3]
    #         print(product_name+" "+product_ch_name+" "+product_version+" "+product_team)
    #         # plat_ver = i_plat_ver.objects.get(name=product_version)
    #         #plat_team = i_app_team.objects.get(name=product_team)
    #         # print(plat_ver)
    #         #print(plat_team)
    #
    #         r=i_plat(
    #             plat_id=product_name
    #             ,plat_name=product_ch_name
    #             ,plat_ver=i_plat_ver.objects.get(name=product_version)
    #             ,plat_name_foreign=''
    #             ,plat_team=i_app_team.objects.get(name=product_team)
    #             ,create_time=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    #         )
    #         try:
    #             r.save()
    #             print("插入成功")
    #         except:
    #             print("表数据已存在，插入异常")


    # r=i_plat(
    #     plat_id='MYTEST1'
    #     ,plat_name='测试'
    #     ,plat_ver=i_plat_ver.objects.get(name='OTHER')
    #     ,plat_name_foreign=''
    #     ,plat_team=i_app_team.objects.get(code='1')
    #     ,create_time=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    # )
    # try:
    #     r.save()
    #     print("插入成功")
    # except:
    #     print("表数据已存在，插入异常")



    for line in i_plat.objects.all():
        print(line)



    req = {
        'title': '巡检监控'
    }
    print(req)
    return render(request, 'monitor_inspection/index.html', req)