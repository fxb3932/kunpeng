from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt    #可post调用url
import json

# Create your views here.
import main

def index(request):
    print('start index rota_day')
    # 权限检查
    auth_data = {
        'request': request
        , 'net': False
        , 'login': True
        , 'perm': 'rjxf_server.add_flow'
    }
    resp_auth = main.auth(auth_data)
    if resp_auth.get('code') == False:
        return render(request, 'alarm/resp.html', {"message": resp_auth.get('msg')})

    req = {
        'title': 'rota_day'
    }
    # print(req)
    return render(request, 'rota_day/index.html', req)

@csrf_exempt
def upload(request):
    readme_info = ''
    print(request.POST.get('file_name'))
    # 通过文件上传方式
    file_obj = request.FILES.get('file', None)
    print(file_obj.name)
    print(file_obj.size)
    print(file_obj.__dict__)

    print(file_obj.name[-4:])

    file_name = file_obj.name
    file_size = str(file_obj.size)
    file_id = ''

    with open('static/app/rota_day/zbb.png', 'wb') as f:
        for line in file_obj.chunks():
            f.write(line)
        message = '上传[' + file_name + ']文件成功，大小[' + file_size + ']'
        code = True
        f.close()

    resp = {
        "file_stat": code
        , "message": message
        , "file_name": file_name
        , "file_size": file_size
        , "file_id": file_id
        , "readme_buff": readme_info
    }
    # os.chdir(_work_path)
    return HttpResponse(json.dumps(resp), content_type="application/json")