from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt  # 可post调用url
import json
from main import connect_mysql
from cmdb.models import user_info


@csrf_exempt
def search_problem_score(request):
    print('start index search_problem_score')

    data = []
    for line in user_info.objects.all():
        data.append({
            'first_name': line.first_name
            , 'score_sum': line.score
        })

    resp = {
        'code': 0
        , 'data': data
    }
    return HttpResponse(json.dumps(resp), content_type="application/json")
