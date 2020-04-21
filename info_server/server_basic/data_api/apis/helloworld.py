from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt    #可post调用url
import json

from django.contrib.auth.models import User
from cmdb.models import *
from myview.models import Article
from django.db.models import Count
import main




@csrf_exempt
def helloworld(request):
    print('start index test')

    # input_data = {
    #     "app_type": "search_problem"
    #     , 'action_type': "search"
    # }
    # tmp = main.action(request, input_data)
    # print(tmp)

    # for line in user_info.objects.all():
    #     r = user_info.objects.get(id=line.id)
    #     r.score = 0
    #     r.save()

    # action.objects

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