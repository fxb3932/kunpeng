from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt    #可post调用url
import json

from django.contrib.auth.models import User
from cmdb.models import *

@csrf_exempt
def helloworld(request):
    print('start index test')

    print(request.POST)
    print(request.POST.get('comm_s_par2'))

    # for line in User.objects.all():
    #     print(line.first_name)
    #     r = user_info(
    #         first_name=line.first_name
    #     )
    #     r.save()

    resp = {
        'code': 0
        , 'a': '中文'
        , 'b': request.POST.get('comm_s_par2')
        , 'c': [
            {'a': 1}
            , {'b': 2}
        ]
    }
    return HttpResponse(json.dumps(resp), content_type="application/json")