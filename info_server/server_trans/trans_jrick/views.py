from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import json

'''
页面跳转

'''


def index(request):
    print('start index trans_jrick')
    req = {
        'aaa': 111
    }
    print(req)
    return render(request, 'trans_jrick/aaa.html', req)


def aaa(request):
    print('start index trans_jrick')
    req = {
        'aaa': 111,
        'msg': "test"
    }
    print(req['aaa'])
    return render(request, 'trans_jrick/aaa.html', req)


def get_trans(request):
    print('start index get_trans')
    req = {
        'aaa': 111,
        'msg': "test"
    }
    print(req['aaa'])
    return render(request, 'trans_jrick/yh_trans.html', req)



from django.views.decorators.csrf import csrf_exempt  # 可post调用url

'''
事件访问
'''


@csrf_exempt
def submit(request):
    # file_name = './log/write_yh.txt'
    # with open(file_name, 'a') as file_obj:
    #     file_obj.write("start submit trans_jrick_test\n")
    #     file_obj.write("---------------1----------------\n")
    #     file_obj.write(request.POST.get('name')+"\n")
    #     file_obj.write("---------------2----------------\n")
    # print('start submit trans_jrick')
    # print("-------------------------------")
    # print(request.POST)
    # print("-------------------------------")
    # print(request.POST.get('title'))


    test = {
        "message": "aaaaaaaaaaa",
        "YH": "12345678"
    }
    msg = json.dumps(request.POST)




    print("--------------------------")
    print("请求的类型:", type(request.POST))
    print("test类型:", type(test))
    print("返回的类型:", type(msg))
    print("--------------------------")

    return HttpResponse(msg)

@csrf_exempt
def submit_new(request):
    # file_name = './log/write_yh.txt'
    # with open(file_name, 'a') as file_obj:
    #     file_obj.write("start submit trans_jrick_test\n")
    #     file_obj.write("---------------1----------------\n")
    #     file_obj.write(request.POST.get('name')+"\n")
    #     file_obj.write("---------------2----------------\n")
    # print('start submit trans_jrick')
    # print("-------------------------------")
    # print(request.POST)
    # print("-------------------------------")
    # print(request.POST.get('title'))


    test = {
        "message": "1111111111111",
        "YH": "222222222222222"
    }
    msg = json.dumps(test)

    print("--------------------------")
    print("请求的类型:", type(request.POST))
    print("test类型:", type(test))
    print("返回的类型:", type(msg))
    print("--------------------------")
    return HttpResponse(msg, content_type="application/json")

@csrf_exempt
def submit_aa(request):
    msg = "bbbbbbbbbbbbbbbb"
    print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    return HttpResponse(msg)

@csrf_exempt
def submit_bb(request):
    print("cccccccccccccccccccccccccccccccccccccccccccccccccccccccccc")
    return HttpResponse("heollo")


@csrf_exempt
def test(request):
    file_name = './log/write_yh.txt'
    with open(file_name, 'a') as file_obj:
        file_obj.write("start submit trans_jrick_test\n")
        file_obj.write("-------------------------------\n")

    print('start submit trans_jrick_test')
    print("-------------------------------")
    print(request.POST)
    print("-------------------------------")
    print(request.POST.get('title'))
    return HttpResponse(json.dumps({"message": "OK", "YH": "HAOSHUAI"}), content_type="application/json")
