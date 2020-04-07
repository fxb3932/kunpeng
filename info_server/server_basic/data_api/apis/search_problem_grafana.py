from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt  # 可post调用url
import json

# import sys
# sys.path.append('server_aiops')


from search_problem.models import info
from search_problem.models import info_stat
from search_problem.models import info_channel
from search_problem.models import info_type
from search_problem.models import action
from django.forms.models import model_to_dict
from django.db.models import Count

import requests
import time


@csrf_exempt
def search_problem_grafana(request):
    print('start index search_problem_grafana')


    resp = {
        "code": 0
        , "status":"success"
    }
    return HttpResponse(json.dumps(resp), content_type="application/json")

@csrf_exempt
def search(request):
    print('start index search_problem_grafana search')

    resp = { 'target': 'upper_50' }
    # resp = ["upper_25","upper_50","upper_75","upper_90","upper_95"]
    print(json.dumps(resp))
    return HttpResponse(json.dumps(resp), content_type="application/json")
