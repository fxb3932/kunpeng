from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt    #可post调用url
import json
from cmdb.models import *
from django.views.generic.base import View
from django.forms.models import model_to_dict
# Create your views here.
import main
def index(request):

    # 权限检查
    # auth_data = {
    #     'request': request
    #     , 'net': False
    #     , 'login': False
    #     , 'perm': ''
    # }
    # resp_auth = main.auth(auth_data)
    # if resp_auth.get('code') == False:
    #     return render(request, 'alarm/resp.html', {"message": resp_auth.get('msg')})

    data = [{'type': 'D', 'title': '开始日期'}, {'type': 'D', 'title': '结束日期'}, {'type': 'I', 'title': '缺失表'}]
    res = {
        'title': '数据分析22',
        'code': 0,
        'msg': ",",
        'count': 3,
        'data': data
    }

    # print(req)
    return render(request, 'sjtq_cib/index.html', res)


class doSjtqView(View):
    def get(self, request):
        return render(request, 'bank_Balance.html')

    def post(self, request):
        return

class queryShellView(View):
    def get(self, request):
        res={'code':'测试成功'}
        return render(request, 'sjtq_cib/queryShell.html',res)

    def post(self, request):
        return

class showResultView(View):
    def get(self, request):
        return render(request, 'bank_Balance.html')

    def post(self, request):
        return
class uploadShellView(View):
    def get(self, request):
        return render(request, 'bank_Balance.html')

    def post(self, request):
        return

def index2(request):
    data=[{'type':'D','title_ch':'开始日期','title':'KSRQ'},{'type':'D','title_ch':'结束日期','title':'QSRQ'},{'type':'I','title_ch':'源表1','title':'ST1'}]
    code = """
    #!/bin/bash
    echo "test"
    """
    file_object = open('/home/insp_ap/zzq/sjtq.sh',"r", encoding='gbk')
    try:
        file_context = file_object.read()
    # file_context = open(file).read().splitlines()

    finally:
        file_object.close()

    req = {
        'title': '数据分析',
        'code': 0,
        'msg': ",",
        'date':'2020-02-24',
        'count': 3,
        'data': data,
         'code':file_context
    }
    return render(request, 'sjtq_cib/index.html', req)

class propertiesView(View):
    def get(self,request):
        pass

    def post(self,request):
        pass