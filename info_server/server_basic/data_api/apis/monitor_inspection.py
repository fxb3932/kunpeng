from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt    #可post调用url
import json


from cmdb.models import *
@csrf_exempt
def monitor_inspection(request):
    print('start api yh_test')

    data = []
    for line in c_config_v1.objects.all():
        data.append(line.app_mode.name)



    data1=[]


    for line in i_bank.objects.all():
        data1.append({
            'name': line.name
            , 'name_ch': line.name_ch
            , 'yhdm': line.yhdm

        })

    for line in c_config_v1.objects.all():

        print(line.__dict__)
        print(line.app_mode.__dict__)
        print(line.app_mode.name)

    r = c_config_v1.objects.get(id=5)
    print(r.plat_id)
    r.app_mode = i_app_mode.objects.get(code=2)
    # r.save()
    # r.delete()




    resp = {
        "code": 0
        , "data": data
        , 'data1': data1
    }
    return HttpResponse(json.dumps(resp), content_type="application/json")

