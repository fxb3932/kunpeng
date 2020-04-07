from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt    #可post调用url
import json

from django.contrib.auth.models import User
from cmdb.models import *
from myview.models import Article
from django.db.models import Count

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

    trans_all_data = []
    tmp = list(Article.objects.all()
               .extra(select={"CreateTime": "date_format(date,'%%m-%%d')"})
               .values('CreateTime')
               .annotate(count=Count('date')))

    for line in tmp:
        print(line)

    # for line in tmp:
    #     trans_all_data.append({
    #         "date": line.get('CreateTime')
    #         , "录入量": line.get('count')
    #         , "访问量": n
    #     })

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