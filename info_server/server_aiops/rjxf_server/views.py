#20191118 make 获取文件列表机制修改为多线程，提高页面加载速度
#20191101 流程管理，新增版本制作时间，下发时间，操作人等
#20191025 准备修改可重新提交同版本功能，在解压及拷贝时做目录的删除操作
#20191025 更新 config_disconvery 增加 plat 字段，支持多产品多租户的使用

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import time

import sys
sys.path.append('../')
import main

shell = main.Shell()

import json

import glob
from django.views.decorators.csrf import csrf_exempt    #可post调用url

### 参数配置 ###
# rjxf_par = [
#     {'ftp_id': 'cib_v3plus', 'ftp_pwd': '/rjxf/v3plus/hxxt'},
#     {'ftp_id': 'cib_czyh', 'ftp_pwd': '/rjxf/czyh/hxxt'},
#     {'ftp_id': 'cib_czyh7.1', 'ftp_pwd': '/rjxf/7.1czyh/hxxt'},
#     {'ftp_id': '5182', 'ftp_pwd': '/rjxf/5182/hxxt'},
#     {'ftp_id': '5169', 'ftp_pwd': '/rjxf/5169/hxxt'},
#     {'ftp_id': '6590', 'ftp_pwd': '/rjxf/6590/hxxt'},
#     {'ftp_id': '44063', 'ftp_pwd': '/rjxf/44063/hxxt'},
#     {'ftp_id': 'V3', 'ftp_pwd': '/rjxf/V3/hxxt'},
# {'ftp_id': '73', 'ftp_pwd': '/rjxf/73/hxxt'},
#     {'ftp_id': 'XA', 'ftp_pwd': '/rjxf/XA/hxxt'}
# ]


# print(rjxf_par)

_tmp_path = '/home/insp_ap/rjxf/rjxf_tmp/'
_new_path = '/home/insp_ap/rjxf/rjxf_file/'

_chk_passwd = 'abcd1234!'
import os
_work_path = os.getcwd()
###############

### 公用方法 ###
import re
from .models import file_dir
from cmdb.models import config_discovery

# config_discovery_data = config_discovery.objects.all()
config_discovery_data = config_discovery.objects.filter(plat="V3_CIB")

file_dir_data = file_dir.objects.all()

def fxb_test(request):
    req = {
        "dir": './cs37033/'
        , "bank_no": ''
        , "plat_id": 'v3_cib'
        , "bank_group": '临沂兰山农村合作银行'
    }
    data = flow.objects.all()
    for line in data :
        print(line.make_date)
    print('--------')
    data = flow.objects.filter(make_date=None)
    for line in data :
        print(line)
        print(line.make_date)
        # line.make_date = '2019-01-01 00:00:00'
        # line.save()
    print(data)
    resp = {
        "req": req
        , "resp": 'isFileOk_test(req)'
    }
    print(resp)
    return HttpResponse(json.dumps(resp), content_type="application/json")

def isFileOk(req):
    print(req)
    clj_type = False

    #前端一些功能，可以直接通过验证
    if req.get('bank_no') == 'NOCHECK':
        return {"stat":True}

    #SGB处理机验证
    if req.get('plat_id') == 'sgb_server':
        if req.get('bank_group')[-3:] == 'CLJ':
            clj_type = True
            if req.get('dir') == './sql/' or req.get('dir') == './cs/' or req.get('dir') == './menu/':
                return {"stat": False, "clj_type": clj_type,
                        "txt": '处理机无需下发[' + req.get('dir').split('/')[1] + ']目录'}
            else:
                print('sgb_server ok')
    #核心V2处理机验证
    if req.get('plat_id') == 'cib':
        if  req.get('bank_group')[-3:] == 'CLJ' :
            clj_type = True
            if req.get('dir') != './so/' and req.get('dir') != './clear/':
                return {"stat": False, "clj_type": clj_type, "txt": '处理机无需下发[' + req.get('dir').split('/')[1] + ']目录'}

    #核心V3 库尔勒APP无需下发 sql / cs 等数据库操作的步骤
    if req.get('plat_id') == 'v3_cib':
        # find 如果包含子字符串返回开始的索引值，否则返回-1。
        if req.get('dir').find('ofep') != -1:
            return {"stat": False, "clj_type": clj_type, "txt": '非 cib 用户下发步骤，需要手工进行下发'}
        # if req.get('bank_group') == 'APP1_库尔勒银行' or req.get('bank_group') == 'APP2_库尔勒银行' :
        if req.get('bank_group')[-3:] == 'CLJ':
            if req.get('dir') == './sql/' or req.get('dir') == './cs/':
                return {"stat": False, "clj_type": clj_type, "txt": 'APP无需下发[' + req.get('dir').split('/')[1] + ']目录'}

    #目录合规验证，通过 file_dir 表中配置的目录进行验证
    for line in file_dir_data:
        if req.get('dir') == './' + line.name + '/':
            return {"stat":True, "clj_type": clj_type}

    #多租户版本验证，当 bank_no 为数组中有匹配通过
    if type(req.get('bank_no')) == list:
        for line in req.get('bank_no'):
            if line == req.get('dir').split('/')[1][-5:]:
                return {"stat":True, "clj_type": clj_type}
    else:
        if req.get('bank_no') == req.get('dir').split('/')[1][-5:]:
            return {"stat":True, "clj_type": clj_type}

    #核心V3特殊版本行号验证
    if req.get('plat_id') == 'v3_cib':
        for line in config_discovery_data:
            if req.get('bank_group') == line.bank_group:
                if line.bank_no == req.get('dir').split('/')[1][-5:]:
                    return {"stat":True, "clj_type": clj_type}



    return {"stat": False, "txt": '非本行银行代码，无需下发', "clj_type": clj_type}

def isFileOk_2(line, bank_no):
    if line == './so/' or line == './cs/' or line == './sql/' or line == './libso/' or line == './other/':
    #if line == './so/' :
        return True
    else:

        # 检查如 cs + YHDM 的特殊版本
        resp = []
        if bank_no == 'NOCHECK':
            return True
        else:
            try:
                resp = re.match('./cs[1-9]\d*/$', line).span()
            except:
                resp.append('err')
                resp.append(0)

            if resp[1] == 10:
                # 行号认证
                if line != './cs' + bank_no + '/':
                    return False

                return True
            else:
                return False

        print(resp)
        return False

def get_replace_color(txt, buff, color):
    txt = txt.replace(buff, "<span style='color:" + color + ";'>" + buff + '</span>')  # 黄色
    return txt

def get_rjxf_file_pwd_list(rjxf_id):
    _now_path = os.getcwd()
    list_sub_dir = []
    os.chdir(_new_path + rjxf_id)
    pathList = glob.glob('./*/')

    # 排序处理
    tmpList = pathSort(pathList, './other/')
    tmpList = pathSort(tmpList, './cs/')
    tmpList = pathSort(tmpList, './sql/')
    tmpList = pathSort(tmpList, './sgb/')
    tmpList = pathSort(tmpList, './so/')
    tmpList = pathSort(tmpList, './libso/')
    pathList = pathSort(tmpList, './clear/')


    for line in pathList:
        req = {
            "dir": line
            , "bank_no": 'NOCHECK'
        }
        if isFileOk(req).get('stat') == True:
            shell_name = 'add' + line.split('/')[1] + '.sh'
            shell_info = get_rjxf_readme(_new_path + rjxf_id + '/' + line.split('/')[1] + '/' + shell_name)
            print('shell_name=[' + shell_name + ']')
            print('shell_info=[' + shell_info + ']')
            shell_rjxf_stat = True
            if line.split('/')[1] == 'ofep':
                shell_rjxf_stat = False
            list_sub_dir.append({
                'name': line.split('/')[1]
                , 'text': shell_name
                , 'id': shell_info
                , 'shell_rjxf_stat': shell_rjxf_stat
                #, 'id': 'mm(){<br>#判断文件是否存在，如果存在则用MV备份。如不存在，则不进行MV操作。'
            })

    # readme_info = get_rjxf_readme(_new_path + rjxf_id + '/readme.txt')
    # list_sub_dir.append({
    #     'name': '安装说明'
    #     , 'text': '安装说明'
    #     , 'id': readme_info
    #     , 'shell_rjxf_stat': True
    #     # , 'id': 'mm(){<br>#判断文件是否存在，如果存在则用MV备份。如不存在，则不进行MV操作。'
    # })
    os.chdir(_now_path)
    return list_sub_dir

@csrf_exempt
def get_rjxf_file_info(request):
    print('in get_rjxf_file_info')
    print(request.POST.get('_rjxf_id'))

    rjxf_file_list = [
        {'id': 'readme_info1', 'text': '安装说明'}
        , {'id': 'readme_info2', 'text': 'addso.sh'}
    ]

    rjxf_file_list = get_rjxf_file_pwd_list(request.POST.get('_rjxf_id'))

    readme_info = get_rjxf_readme(_tmp_path + request.POST.get('_rjxf_id') + '/readme.txt')
    rjxf_file_list.insert(0, {'id': readme_info, 'text': '安装说明'})



    resp = {
        "resp": 'ok'
        , "rjxf_file_list": rjxf_file_list
    }
    print(resp)
    return HttpResponse(json.dumps(resp), content_type="application/json")
###############

def rjxf_tab_txt(txt):
    txt = txt.replace('"', '')
    txt = txt.replace("'", '')
    txt = txt.replace('\n', '<br>')
    txt = txt.replace("\\", '')
    txt = txt.replace("\t", '')
    txt = txt.replace("\r", '')
    txt = txt.replace("\002", '')
    txt = txt.replace('~', '')

    arr_tmp_txt = []
    for line in txt.split('<br>'):
        if line != '':
            arr_tmp_txt.append(line)

    txt = '<br>'.join(arr_tmp_txt)


    return txt

def get_rjxf_readme(file_name):
    print('get_rjxf_readme [' + file_name + ']')
    with open(file_name, "r", encoding='gbk') as f:
        readme_buff = ''.join(f.readlines())
        print(readme_buff)
        f.close()

        #文本特殊处理
        readme_buff = readme_buff.replace('\n', '<br>')
        # readme_buff = rjxf_tab_txt(readme_buff)
        # 黄色
        for line in file_dir_data:
            readme_buff = get_replace_color(readme_buff, line.name, '#FFE500')

        # 黄色 加粗 忽略大小写
        for line in ['该版本目录下未找到安装说明！']:
            readme_buff = re.sub(line, "<span style='color:#FFE500;'><strong>" + line + "</strong></span>", readme_buff, flags=re.IGNORECASE)

        # 蓝色
        for line in ['add', '.sh', '.log']:
            readme_buff = get_replace_color(readme_buff, line, '#00D5FF')

        # 红色加粗 忽略大小写
        for line in ['hosts', 'services', 'ofep', 'dlpt.cfg', 'tmsync', '调度库', 'crontab', 'hzcx', 'cp', 'tar', 'whyz', 'mkdir']:
            readme_buff = re.sub(line, "<span style='color:#E53333;'><strong>" + line + "</strong></span>", readme_buff, flags=re.IGNORECASE)

        readme_buff = '<div style="padding: 50px; line-height: 22px; background-color: #393D49; color: #fff; font-weight: 300;">' + readme_buff + '</div>'
        # readme_buff = readme_buff.replace('"', '\'')
        print(readme_buff)
    return readme_buff
###############

def test(request):
    return render(request, 'rjxf_server/test.html')

from django.contrib.auth.models import User
from .models import ftp_path
import threading

file_list = []
class forThread_make(threading.Thread):
    def __init__(self, event):
        threading.Thread.__init__(self)
        self.name = 'myThread'
        self.event = event

    def run(self):
        print(self.event.get('a'))
        resp = shell.runCmd('sh ./server_aiops/rjxf_server/shell/get_dir.sh ' + \
                            self.event.get('ftp_pwd'))


        for line in resp[1].decode('gbk').replace('\r', '').split('\n'):
            if line != '*.tar':
                file_list.append({"name": line
                                     , 'id': self.event.get('ftp_id')
                                     , 'pwd': self.event.get('ftp_pwd')
                                  })


def make(request):
    print('start index make')
    user = request.user
    print(user)

    # 权限检查
    auth_data = {
        'request': request
        , 'net': False
        , 'login': True
        , 'debug': True
        , 'perm': 'rjxf_server.add_flow'
    }
    resp_auth = main.auth(auth_data)
    print('user : ' + request.user.first_name)
    if resp_auth.get('code') == False : return render(request, 'alarm/resp.html', {"message": resp_auth.get('msg')})
    file_list.clear()
    i = 1
    for rjxf_line in ftp_path.objects.all():
        print(rjxf_line)
        print(rjxf_line.ftp_id)

        # 多线程不增加 sleep 的情况下 expect 会出现异常
        sleep(0.02)

        data = {
            'ftp_id': rjxf_line.ftp_id
            , 'ftp_pwd': rjxf_line.ftp_pwd
        }

        exec('thread{} = forThread_make(data)'.format(i))
        exec('thread{}.start()'.format(i))
        i += 1

    x = 1
    while x < i :
        exec('thread{}.join()'.format(x))
        x += 1

    s_date = time.strftime('%Y-%m-%d', time.localtime())
    req = {
        'title': '软件下发版本制作'
        , 'date': s_date
        # , 'req': list_req
        , 'file_list': file_list
        , 'user_list': User.objects.all()

    }
    # print(req)
    return render(request, 'rjxf_server/make.html', req)



#_tmp_path = 'rjxf_server/static/tmp/'
#_new_path = 'rjxf_server/static/rjxf_file/'




# 一级交易查询---本地查询


@csrf_exempt
def upload(request):
    try:

        readme_info = ''
        print(request.POST.get('file_name'))
        # 通过文件上传方式
        if request.POST.get('file_name') == None:
            file_obj = request.FILES.get('file', None)
            print(file_obj.name)
            print(file_obj.size)
            print(file_obj.__dict__)

            print(file_obj.name[-4:])


            file_name = file_obj.name
            file_size = str(file_obj.size)
            file_id = ''
        else:
            file_all_name = request.POST.get('file_name')
            file_name = file_all_name.split('/')[-1]
            file_id = ''
            shell_resp = shell.runCmd('sh ./server_aiops/rjxf_server/shell/get_file.sh ' + file_all_name)
            print('##### get_file.sh start #####')
            print(shell_resp[1].decode('gbk'))
            print('##### END #####')
            resp = shell.runCmd('ls -trl ' + _tmp_path + file_name + "|awk '{print $5}'")
            file_size = resp[1].decode('gbk')
            message = '上传[' + file_name + ']文件成功，大小[' + file_size + ']'
            code = True

        try:
            #file_id = file_name.split('Patch_')[1].split('.')[0]
            file_id = file_name.split('Patch_')[1].rstrip('.tar')
        except:
            raise EOFError('不满足上传文件格式要求：系统_Patch_版本号.tar')

        if file_name[-4:] != '.tar':
            raise EOFError('文件格式异常，下发包必须为tar格式')

        shell.runCmd('mkdir -p ' + _tmp_path)
        shell.runCmd('mkdir -p ' + _new_path)
        os.chdir(_tmp_path)

        if request.POST.get('file_name') == None:
            with open(file_name, 'wb') as f:
                for line in file_obj.chunks():
                    f.write(line)
                message = '上传[' + file_name + ']文件成功，大小[' + file_size + ']'
                code = True
                f.close()

        cmd_1 = 'rm -rf ' + _tmp_path + file_id
        shell.runCmd(cmd_1)
        cmd_2 = 'tar xvf ' + file_name
        resp = shell.runCmd(cmd_2)[1].decode('GBK').split('\n')

        shell_resp = shell.runCmd('sh ' + _work_path + '/server_aiops/rjxf_server/shell/mv_readme.sh ' + _tmp_path + file_id)
        print('##### mv_readme.sh start #####')
        print(shell_resp[1])
        print('##### END #####')
        # print(resp)

        print('开始检查下发包内容：')
        os.chdir(file_id)

        print('step1 安装说明')
        print(shell.runCmd('ls')[1].decode('gbk'))
        print(shell.runCmd('pwd')[1].decode('gbk'))

        #print(readme_file_name)
        # with open('readme.txt', "r", encoding='gbk') as f:
        #     readme_buff = ''.join(f.readlines())
        #     print(readme_buff)
        #     f.close()

        # readme_info = get_rjxf_readme(_tmp_path + file_id + '/readme.txt')
        with open(_tmp_path + file_id + '/readme.txt', "r", encoding='gbk') as f:
            readme_info = ''.join(f.readlines())

        print('step2 标准检查')
        pathList = glob.glob('./*/')
        for line in pathList :
            req = {
                "dir": line
                , "bank_no": 'NOCHECK'
            }
            if isFileOk(req).get('stat') == True:
                print('check ' + line)
                fileList = glob.glob(line + '*')
                print(fileList)
                runShellName = line + 'add' + line.split('/')[1] + '.sh'


                if line == './menu/':   # sgb 版本 menu 目录特殊化合规检查
                    if './menu/menu.txt' not in fileList:
                        raise EOFError('./menu/menu.txt not find')  #版本制作时上传文件提示
                    else:
                        # 自动生成 addmenu.sh 脚本
                        cmd = 'cp ' + _work_path + '/server_aiops/rjxf_server/shell/addmenu.sh ./menu/addmenu.sh'
                        print(cmd)
                        shell.runCmd(cmd)
                else:
                    if runShellName not in fileList:
                        raise EOFError(runShellName + ' not find')
            else:
                raise EOFError('检查到未登记的下发目录[' + line + ']请联系开发人员')



    except Exception as msg:
        print(type(msg))
        print(msg)
        message = str(msg)
        code = False

    resp = {
        "file_stat": code
        , "message": message
        , "file_name": file_name
        , "file_size": file_size
        , "file_id": file_id
        , "file_path": _new_path
        , "readme_buff": readme_info
    }
    os.chdir(_work_path)
    return HttpResponse(json.dumps(resp), content_type="application/json")

from cmdb.models import config

@csrf_exempt
def post_tree(request):
    tree_data = [{
        'id': 'v3_cib', 'title': '核心V3'
        # , 'checked': True     #是否选中
        , 'spread': True      #是否展开
        , 'children': [
            {'id': 'v3_cib:LNZX', 'title': '服务器A', 'ip': '11.11.11.11'}
            , {'id': 'v3_cib:SNYH', 'title': '服务器B', 'ip': '22.22.22.22'}
        ]
    }, {
        'id': 'v2_cib', 'title': '核心V2'
        # , 'checked': True     #是否选中
        , 'spread': True  # 是否展开
        , 'children': [
            {'id': 'v2_cib:AIX7.1', 'title': 'AIX7.1', 'spread': True, 'children': [{'id': 'v2_cib:AIX7.1:LNZX', 'title': '服务器A', 'ip': '33.33.33.33'}]}
            , {'id': 'v2_cib:AIX5.4', 'title': 'AIX5.4', 'spread': True, 'children': [{'id': 'v2_cib:AIX5.4:SNYH', 'title': '服务器A', 'ip': '44.44.44.44'}]}
        ]
    }]

    # class config(models.Model):
    #     plat_id = models.CharField(max_length=128)
    #     plat_name = models.CharField(max_length=128)
    #     name_ch = models.CharField(max_length=128)
    #     name = models.CharField(max_length=32)
    #     sys = models.CharField(max_length=64)
    #     ip = models.CharField(max_length=32)
    #     user
    #     #passwd = models.CharField(max_length=64, blank=True, null=True)
    #     team = models.CharField(max_length=128, blank=True, null=True)
    #     worker = models.CharField(max_length=64, blank=True, null=True)
    #     bank = models.CharField(max_length=64, blank=True, null=True)
    #     port = models.CharField(max_length=64)
    #     ver = models.CharField(max_length=128, blank=True, null=True)
    tree_data = []
    set_data = set([])
    i = -1
    set_data_3 = set([])
    i_3 = -1

    for line in config.objects.all().order_by('plat_id', 'ver'):
    #for line in config.objects.all():
        #print(line.plat_id + ':' + line.plat_name + ':' + line.name_ch)
        # 二级列表
        #print(line)
        if line.ver == '':
            if line.plat_id not in set_data:
                tree_data.append({
                    'id': line.plat_id
                    , 'title': line.plat_name
                    , 'spread': False  # 是否展开
                    , 'children': []
                })
                i += 1

            tree_data[i]['children'].append({
                'id': line.plat_id + line.name
                , 'title': line.name_ch + '_' + line.name
                , 'name_ch': line.name_ch
                , 'name': line.name
                , 'sys': line.sys
                , 'ip': line.ip
                , 'user': line.user
                , 'team': line.team
                , 'worker': line.worker
                , 'bank': line.bank
                , 'port': line.port
                , 'ver': line.ver
            })
        # 三级列表
        else:
            if line.plat_id not in set_data:
                tree_data.append({
                    'id': line.plat_id
                    , 'title': line.plat_name
                    , 'spread': False  # 是否展开
                    , 'children': []
                })
                # print(line.plat_id)

                set_data_3 = set([])
                i += 1
                i_3 = -1

            # print(set_data_3)
            if line.ver not in set_data_3:
                tree_data[i]['children'].append({
                    'id': line.plat_id + line.name
                    , 'title': line.ver
                    , 'spread': False  # 是否展开
                    , 'children': []
                })
                i_3 += 1

            # print(str(i) + ':' + str(i_3))
            tree_data[i]['children'][i_3]['children'].append({
                'id': line.ver + line.plat_id + line.name
                , 'title': line.name_ch + '_' + line.name
                , 'name_ch': line.name_ch
                , 'name': line.name
                , 'sys': line.sys
                , 'ip': line.ip
                , 'user': line.user
                , 'team': line.team
                , 'worker': line.worker
                , 'bank': line.bank
                , 'port': line.port
                , 'ver': line.ver
            })

            set_data_3.add(line.ver)

        set_data.add(line.plat_id)
    resp = {
        "code": 0,
        "tree_data": tree_data
    }
    #print(resp)
    return HttpResponse(json.dumps(resp), content_type="application/json")
# 二级交易查询---联动查询
from .models import flow

# def list_all_dict(dict_a):
#     if isinstance(dict_a, dict):  # 使用isinstance检测数据类型
#         for x in range(len(dict_a)):
#             temp_key = dict_a.keys()[x]
#             temp_value = dict_a[temp_key]
#             print("%s : %s" % (temp_key, temp_value))
#             list_all_dict(temp_value)  # 自我调用实现无限遍历

list_all_dict_data = []
def list_all_dict(input_list):
    if type(input_list) == list:
        for line in input_list:
            if type(line.get('children')) == list:
                list_all_dict(line.get('children'))
            else:
                # print(line)
                list_all_dict_data.append(line)


from django.contrib.auth.models import auth

@csrf_exempt
def submit(request):
    msg = 'ok'
    r_save_stat = False
    try:
        print(request.POST)
        print(json.loads(request.POST.get('input_data')).get('date'))
        input_data = json.loads(request.POST.get('input_data'))
        tree_data = json.loads(request.POST.get('tree_data'))
        try:
            file_data = json.loads(request.POST.get('file_data'))[0]
        except :
            file_data = {}

        print(input_data)
        print(tree_data)
        print('-------')
        # 将多层数组转换为单维数组，用于统计选择的合作行数量
        list_all_dict_data.clear()
        list_all_dict(tree_data)
        print(list_all_dict_data)
        print(len(list_all_dict_data))
        # for line_1 in tree_data:
        #     print(line_1)
        #     # print(line_1.get('children'))
        #     for line_2 in line_1.get('children'):
        #         print(line_2)
        #         if type(line_2.get('children')) == list:
        #             for line_3 in line_2.get('children'):
        #                 print(line_3)
        print('-------')
        print(file_data)
        print(file_data.get('file_name'))
        chk_username = ''

        if tree_data == []:
            msg = '下发范围不能为空，请重新选择！'
            return HttpResponse(json.dumps({"message": str(msg)}), content_type="application/json")

        if file_data.get('file_stat') != True:
            msg = '未正确上传版本文件！'
            return HttpResponse(json.dumps({"message": str(msg)}), content_type="application/json")

        chk_user = auth.authenticate(username=input_data.get('chk_username'), password=input_data.get('chk_password'))
        print('chk_user:')
        print(chk_user)
        if chk_user is not None:
            chk_username = chk_user.first_name
            print('chk_username=' + chk_username)
            if chk_user.has_perm('rjxf_server.change_flow') == False:
                msg = '复核人无权限进行授权'
                return HttpResponse(json.dumps({"message": str(msg)}), content_type="application/json")

            if request.user.first_name == chk_user.first_name:
                msg = '不能自已给自已授权哟'
                return HttpResponse(json.dumps({"message": str(msg)}), content_type="application/json")
        else:
            msg = '复核人用户密码输入错误，请注意大小写'
            return HttpResponse(json.dumps({"message": str(msg)}), content_type="application/json")
        if msg == 'ok':
            # 记库

            r = flow(
                date=input_data.get('date') + ' ' + input_data.get('time')
                , rjxf_id=file_data.get('file_id')
                , rjxf_type=input_data.get('rjxf_type')
                , rjxf_txt=input_data.get('rjxf_txt')
                , file_name=file_data.get('file_name')
                , file_size=file_data.get('file_size')
                , rjxf_num_count=len(list_all_dict_data)
                , make_date=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
                , make_oper=request.user.first_name
                , update_oper=input_data.get('update_oper')
                , itsm_no=input_data.get('itsm_no')
                , make_chk_oper=chk_username
            )
            print(r)
            try:
                r.save()
                r_save_stat = True
            except:
                raise EOFError(file_data.get('file_id') + '该版本流程已存在，不得重复建立！')

            # try:
            # 版本提交

            #清理版本目录及结果目录
            shell.runCmd('rm -rf ' + _new_path + file_data.get('file_id'))
            shell.runCmd('rm -rf ' + _new_path + file_data.get('file_id') + '_resp')

            resp = shell.runCmd('cp -r ' + _tmp_path + file_data.get('file_id') + ' ' + _new_path)[
                1].decode('GBK').split('\n')
            print(resp)



            # 保存下发范围
            json_file_name = file_data.get('file_path') + file_data.get('file_id') + '/rjxf_scope.json'
            print(json_file_name)
            f_resp = open(json_file_name, 'w', encoding='utf-8')
            json.dump(tree_data, f_resp, ensure_ascii=False, indent=4)

        else:
            msg = '流程提交失败！'

    except Exception as msg :
        if r_save_stat == True:
            r.delete()
            print('r delete ok')
        print(type(msg))
        print(msg)
        return HttpResponse(json.dumps({"msg_type": str(type(msg)),"message": str(msg)}), content_type="application/json")



    return HttpResponse(json.dumps({"msg_type": str(type(msg)),"message": str(msg)}), content_type="application/json")


def show(request):
    print('start index make')

    # 权限检查
    auth_data = {
        'request': request
        , 'net': False
        , 'login': True
        , 'perm': ''
    }
    resp_auth = main.auth(auth_data)
    if resp_auth.get('code') == False:
        return render(request, 'alarm/resp.html', {"message": resp_auth.get('msg')})

    req = {
        'title': '软件下发流程管理'
    }
    return render(request, 'rjxf_server/show.html', req)

@csrf_exempt
def show_get(request):
    print('run show_get')
    t1 = time.time()

    flow_data = flow.objects.all()
    # print(flow_data)
    sub_data = []
    n = 0

    for line in flow_data:
        # print(line.file_name)
        sub_data.append({
            "rjxf_id": line.rjxf_id
            , "rjxf_type": line.rjxf_type
            , "date": str(line.date)[:-3]
            , "rjxf_txt": line.rjxf_txt
            , "rjxf_stat": line.rjxf_stat
            , "chk_stat": line.chk_stat
            , "rjxf_num_count": line.rjxf_num_count
            , 'make_date': str(line.make_date)
            , 'update_date': str(line.update_date)
            , 'update_oper': line.update_oper
            , 'itsm_no': line.itsm_no
        })
        n += 1

    sub_data.sort(key=lambda item: item.get('rjxf_id'), reverse=True)
    sub_data.sort(key=lambda item: item.get('make_date'), reverse=True)

    t2 = time.time()
    t3 = (t2 - t1) * 1000
    print(str(t3))
    data = {
        "code": 0,
        "msg": "",
        "count": n,
        "data": sub_data
    }
    return HttpResponse(json.dumps(data), content_type="application/json")

from .function.fxb import pathSort
@csrf_exempt
def release(request):
    print('in release')
    #print(request.POST)
    #print(request.GET)

    # 权限检查
    auth_data = {
        'request': request
        , 'net': False
        , 'login': True
        , 'debug': False
        , 'perm': 'rjxf_server.change_flow'
    }
    resp_auth = main.auth(auth_data)
    if resp_auth.get('code') == False:
        return render(request, 'alarm/resp.html', {"message": resp_auth.get('msg')})

    rjxf_id = request.GET.get('rjxf_id')
    flow_data = flow.objects.filter(**{'rjxf_id': rjxf_id})
    try:
        post_data = json.loads(request.POST.get("data"))

        for line in post_data:
            print(line)
    except:
        print('...')

    # 需要获取待下发目录列表
    list_sub_dir = []
    list_sub_dir = get_rjxf_file_pwd_list(request.GET.get('rjxf_id'))
    # os.chdir(_new_path + request.GET.get('rjxf_id'))
    # pathList = glob.glob('./*/')
    #
    # # 排序处理
    # tmpList = pathSort(pathList, './cs/')
    # tmpList = pathSort(tmpList, './sql/')
    # pathList = pathSort(tmpList, './so/')
    # print(pathList)
    # try:
    #     pathList.remove('./ofep/')
    # except:
    #     print('无非CIB操作')
    #
    # for line in pathList:
    #     if isFileOk(line, 'NOCHECK') == True:
    #         shell_name = 'add' + line.split('/')[1] + '.sh'
    #         shell_info = get_rjxf_readme(_new_path + rjxf_id + '/' + line.split('/')[1] + '/' + shell_name)
    #         print('shell_name=[' + shell_name + ']')
    #         print('shell_info=[' + shell_info + ']')
    #         list_sub_dir.append({
    #             'name': line.split('/')[1]
    #             , 'text': shell_name
    #             , 'id': shell_info
    #         })

    readme_info = get_rjxf_readme(_new_path + rjxf_id + '/readme.txt')

    req = {}
    for line in flow_data:
        req = {
            "rjxf_id": line.rjxf_id
            , "rjxf_type": line.rjxf_type
            , "date": str(line.date)[:-3]
            , "rjxf_txt": line.rjxf_txt
            , "rjxf_stat": line.rjxf_stat
            , "chk_stat": line.chk_stat
            , 'file_size': line.file_size
            , "list_sub_dir": list_sub_dir
            , "readme_buff": readme_info

        }

    os.chdir(_work_path)
    return render(request, 'rjxf_server/release.html', req)

@csrf_exempt
def post_rjxffw_table_data(request):
    print('in post_rjxffw_table_data')
    print(request.GET)
    rjxf_id = request.GET.get('rjxf_id')
    print(rjxf_id)
    with open(_new_path + rjxf_id + '/rjxf_scope.json', "r", encoding='utf-8') as f:
        f_json = json.load(f)
    # print(f_json)
    sub_data = []
    n = 0
    for line in f_json:
        # print(line.get('id'))
        # print(line.get('title'))
        # print(line.get('children'))
        if line.get('children') != []:
            for line_1 in line.get('children'):
                print(line_1.get('id'))
                print(line_1)
                if line_1.get('children') != []:
                    table_info = {}
                    try:
                        for line_2 in line_1.get('children'):
                            # print(line_2.get('id'))
                            # print('ADD2' + line_2.get('ip'))
                            table_info = {
                                "id": line.get('id')
                                , "sub_id": line_2.get('id')
                                , "title": line_2.get('title')
                                , 'name_ch': line_2.get('name_ch')
                                , 'name': line_2.get('name')
                                , 'sys': line_2.get('sys')
                                , 'ip': line_2.get('ip')
                                , 'user': line_2.get('user')
                                , 'team': line_2.get('team')
                                , 'worker': line_2.get('worker')
                                , 'bank': line_2.get('bank')
                                , 'port': line_2.get('port')
                                , 'ver': line_2.get('ver')
                                , "LAY_CHECKED": True
                            }
                            sub_data.append(table_info)
                    except:
                        # print('ADD1' + line_1.get('ip'))
                        table_info = {
                            "id": line.get('id')
                            ,"sub_id": ''
                            , "title": line_1.get('title')
                            , 'name_ch': line_1.get('name_ch')
                            , 'name': line_1.get('name')
                            , 'sys': line_1.get('sys')
                            , 'ip': line_1.get('ip')
                            , 'user': line_1.get('user')
                            , 'team': line_1.get('team')
                            , 'worker': line_1.get('worker')
                            , 'bank': line_1.get('bank')
                            , 'port': line_1.get('port')
                            , 'ver': line_1.get('ver')
                        }
                        #获取AGENT信息
                        #获取下发信息
                        #print(chk_xf_stat(request.GET.get('rjxf_id'), table_info))
                        isRjxfStat = chk_xf_stat(request.GET.get('rjxf_id'), table_info)
                        if isRjxfStat[0] == False:
                            table_info = dict(table_info, **{'rjxf_stat': '0'})
                        else:
                            #print('---diff---')
                            #print(isRjxfStat[1])
                            #print('RUN_COMMAND_RJXF')
                            if isRjxfStat[1] == ['RUN_COMMAND_RJXF\n']:
                                tmp = '1'
                            else:
                                tmp = isRjxfStat[1]
                            table_info = dict(table_info, **{'rjxf_stat': tmp})
                        sub_data.append(table_info)

    data = {
        "code": 0,
        "msg": "",
        "count": n,
        "data": sub_data
    }
    return HttpResponse(json.dumps(data), content_type="application/json")


from .function.fxb import chk_xf_stat
from .function.fxb import chk_xf_line_stat
#下发接口
@csrf_exempt
def post_xf_command(request):
    print('in post_xf_command start')
    print('post')
    print(request.POST)
    print('get')
    print(request.GET)

    print(request.POST.get('rjxf_id'))
    print(request.POST.get('rjxf_dir'))

    post_data = json.loads(request.POST.get("data"))

    print(_new_path)

    file_rjxf_resp = _new_path + request.POST.get('rjxf_id') + '_resp/'
    cmd = 'mkdir -p ' + file_rjxf_resp
    print(cmd)
    shell.runCmd(cmd)

    print('rjxf_id = ' + request.POST.get('rjxf_id'))

    for line in post_data:
        print(line)
        msg = []


        # 检查是否已下发
        pathListName = './' + request.POST.get('rjxf_dir') + '/'
        print(pathListName)

        req = {
            "dir": pathListName
            , "bank_no": line.get('team')
            , "plat_id": line.get('id')
            , "bank_group": line.get('name_ch')
        }
        if isFileOk(req).get('stat') == False:
            msg.append('无需执行!')
            continue
        elif chk_xf_line_stat(request.POST.get('rjxf_id'), line, pathListName)[0] == True:
            msg.append('已执行过，不可重复提交!')
            continue

        else:
            print('开始执行下发')

        # scp 将版本包推送至 ./rjxf 目录下
        # scp -r $sWorkPwd/$_plat/$_edit $_user@$_ip:./rjxf 2>&1
        #shell.runCmd('scp -r ' + _new_path + request.POST.get('rjxf_id') + ' ' + line.user + '@' + line.ip + ':./rjxf')
        rjxf_path = '\$HOME/rjxf'
        cmd = 'check[run_command:user:mkdir:' + rjxf_path + ']'
        print(cmd)
        resp_cmd = shell.getKey(cmd, line.get('ip'), line.get('port'))[1].decode('gbk').rstrip('\n')
        print('resp_cmd = [' + resp_cmd + ']')
        cmd = 'scp -r ' + _new_path + request.POST.get('rjxf_id') + ' ' + line.get('user') + '@' + line.get('ip') + ':' + rjxf_path
        print(cmd)
        shell.runCmd(cmd)

        # 调用 run_command 执行下发包
        print('开始检查下发包内容：')
        os.chdir(_new_path + request.POST.get('rjxf_id'))
        pathList = glob.glob('./*/')
        pathList = [pathListName]
        print(pathList)
        for line_file in pathList:
            print("line.get('team') = " + line.get('team'))
            print('check ' + line_file)
            fileList = glob.glob(line_file + '*')
            print(fileList)
            runShellName = line_file + 'add' + line_file.split('/')[1] + '.sh'
            print('runShellName = ' + runShellName)

            if runShellName not in fileList:
                raise EOFError(runShellName + ' not find')

            # 保存结果文件
            sFileName = file_rjxf_resp + runShellName.split('/')[2] + '_' + line.get('name') + '_' + line.get(
                'ip') + '.resp'
            print('file_rjxf_resp = ' + file_rjxf_resp)
            req = {
                "dir": line_file
                , "bank_no": line.get('team')
                , "plat_id": line.get('id')
                , "bank_group": line.get('name_ch')
            }
            if isFileOk(req).get('stat') == True:

                try:
                    f_check = open(sFileName, 'r')
                    lines = f_check.readline()
                    print('已下发过，不做处理')
                    f_check.close()
                except FileNotFoundError:
                    print('验证未下发，开始执行远程下发：')

                    #V2核心处理机 addso.sh 特殊处理
                    print('处理机标识：')
                    print(isFileOk(req))

                    cmd_rjxf_path = rjxf_path + '/' + request.POST.get('rjxf_id') + line_file.lstrip('.')
                    cmd_rjxf_run_file = 'add' + line_file.split('/')[1] + '.sh'

                    #clj_type 为处理机标识，为 True 时 run_command_rjxf 会进行处理机替换步骤
                    cmd = 'check[run_command_rjxf:user:' + cmd_rjxf_path + \
                          ':' + cmd_rjxf_run_file + ':' + str(isFileOk(req).get('clj_type')) + \
                            ']'
                    print('rjxf cmd = ' + cmd)
                    resp = shell.getKey(cmd, line.get('ip'), line.get('port'))
                    print('stat:' + str(resp[0]))
                    # print(resp[1].decode('gbk'))
                    msg.append(runShellName + '执行结果：<br>')
                    msg.append(resp[1].decode('gbk'))
                    msg.append('<br>')




                    print(sFileName)
                    if resp[1].decode('gbk') == 'RUN_COMMAND_RJXF\n':
                        f = open(sFileName, 'w')
                        #f.write(resp[1].decode('gbk'))
                        f.write(resp[1].decode('gbk'))
                        f.close()
            else:
                f = open(sFileName, 'w')
                f.write('NOT_NEED_RJXF\n')
                f.close()


        print('循环')
    print('for end')





    data = {
        "msg": ''.join(msg).replace('\n', '<br>')
    }

    os.chdir(_work_path)
    return HttpResponse(json.dumps(data), content_type="application/json")

list_info = []
from time import sleep
class forThread(threading.Thread):
    def __init__(self, event):
        threading.Thread.__init__(self)
        self.name = 'myThread'
        self.event = event

    def run(self):
        # sleep(5)
        #print(self.event)
        # table_resp.append({'index': 'bbb2', 'data': [line]})
        print(self.event)
        os.chdir(_new_path + self.event.get('rjxf_id'))
        # rint(line.get('name'))
        line_file_dict = {}
        for line_file in self.event.get('list_sub_dir'):
            #cmd = 'vfs.file.contents[/home/jgbs/rjxf/' + self.event.get('rjxf_id') + '/' + line_file + '/add' + line_file + '.log]'
            cmd = 'check[run_command:user:cat:\$HOME/rjxf/' + self.event.get(
                'rjxf_id') + '/' + line_file + '/add' + line_file + '.log]'
            resp_msg = ''
            list_bank_no = self.event.get('line').get('team')
            req = {
                "dir": './' + line_file + '/'
                , "bank_no": list_bank_no
                , "plat_id": self.event.get('line').get('id')
                , "bank_group": self.event.get('line').get('name_ch')
            }
            # req = {
            #     "dir": './' + line_file + '/'
            #     , "bank_no": 'NOCHECK'
            # }
            if isFileOk(req).get('stat') == True:
                print(cmd)
                resp = shell.getKey(cmd, self.event.get('line').get('ip'), self.event.get('line').get('port'))
                try:
                    resp_msg = resp[1].decode('gbk', "replace")
                except:
                    resp_msg = str(resp[1])
                print(resp_msg)
                resp_msg = rjxf_tab_txt(resp_msg)
            else:
                #resp_msg = '非本行银行代码，无需下发'
                resp_msg = isFileOk(req).get('txt')

            add_dict = {line_file: resp_msg}
            line_file_dict = dict(line_file_dict, **add_dict)
        list_info.append(dict(self.event.get('line'), **line_file_dict))

@csrf_exempt
def post_resp(request):
    print('in post_resp')

    msg = 'ok'
    list_resp = [
        {'id': 'a1<br>a2', 'text': 'so-2'},
        {'id': 'a2', 'text': 'so-4'},
        {'id': 'a3', 'text': 'so-1'},
        {'id': 'a4', 'text': 'bbb4'}
    ]

    table_resp = [{
        'index': 'so-2'
        , 'data': [
            {'ip': '11.11'}
            , {'ip': '22.22'}
        ]
    }]

    # print(request.GET)
    print(request.POST.get('rjxf_id'))
    list_sub_dir = json.loads(request.POST.get("list_sub_dir"))
    # print(list_sub_dir)
    post_data = json.loads(request.POST.get("data"))
    # print(post_data)


    # for list_sub_dir_line in list_sub_dir:
    #     print(list_sub_dir_line)

    # list_resp = []
    list_info.clear()
    n = 1
    for line in post_data:
        # print(line)
        # print(i)
        data = {
            "rjxf_id": request.POST.get('rjxf_id')
            # 2019-11-06 增加默认选中
            # , "line": line
            , "line": dict(line, **{'LAY_CHECKED': True})
            , "list_sub_dir": list_sub_dir
        }
        exec('thread{} = forThread(data)'.format(n))
        exec('thread{}.start()'.format(n))
        n += 1

    x = 1
    while x < n:
        exec('thread{}.join()'.format(x))
        x += 1

    print(list_info)

    # for line in post_data:
    #     # print(line)
    #     table_resp.append({'index': 'bbb2', 'data': [line]})
    #     os.chdir(_new_path + request.POST.get('rjxf_id'))
    #     # rint(line.get('name'))
    #     line_file_dict = {}
    #     for line_file in list_sub_dir:
    #         cmd = 'vfs.file.contents[/home/amlserver/rjxf/' + request.POST.get('rjxf_id') + '/'+ line_file + '/add' + line_file + '.log]'
    #
    #         print(cmd)
    #         resp = shell.getKey(cmd, line.get('ip'), line.get('port'))
    #         print(resp[1].decode('gbk'))
    #         add_dict = {line_file: resp[1].decode('gbk').replace('\n', '<br>')}
    #         line_file_dict = dict(line_file_dict, **add_dict)
    #     list_info.append(dict(line, **line_file_dict))



    resp_count = {}
    for line_dir in list_sub_dir:
        set_resp = set([])
        dict_resp_tmp = []
        table_count = []
        # print('line_dir = ' + line_dir)

        for line in list_info:
            # print(line.get(line_dir))

            # print('比对开始：')
            if line.get(line_dir) not in set_resp:
                # print('not in')

                # 是否开始标签面的浮动提示
                color = '#5cff3b'
                print('line.get(line_dir)')
                print('[' + line.get(line_dir) + ']')
                try:
                    re.match('cat.*log', line.get(line_dir)).span()
                    color = '#ff243b'
                except:
                    color = '#5cff3b'
                # if 'cat' in line.get(line_dir):
                #     color = '#ff243b'
                dict_resp_tmp.append({
                    'text': 1
                    , 'id': line.get(line_dir)
                    , 'tooltip': line.get(line_dir)
                    , 'style' : "background-color: " + color
                })
                # dict_resp_tmp.append({'text': 1, 'id': line.get(line_dir)})

                table_count.append({
                    'index': line.get(line_dir)
                    , 'data': [line]
                })

                set_resp.add(line.get(line_dir))
            else:
                # print('in')
                x = 0
                y = 0

                for dict_line in dict_resp_tmp:
                    if dict_line.get('id') == line.get(line_dir):
                        dict_resp_tmp[x]['text'] += 1

                    x += 1

                for table_line in table_count:
                    if table_count[y].get('index') == line.get(line_dir):
                        table_count[y]['data'].append(line)
                    y += 1



            z = 0
            # print(dict_resp_tmp)
            dict_resp_tmp.sort(key=lambda item: item.get('text'), reverse=True)
            dict_resp_tmp_str = []
            for int_conv in dict_resp_tmp:
                #print(int_conv)
                dict_resp_tmp_str.append({
                    'text': line_dir + '-' + str(dict_resp_tmp[z]['text'])
                    , 'id': dict_resp_tmp[z]['id']
                })
                # dict_resp_tmp[z]['text'] = 'aaa'
                z += 1

            dict_resp_tmp_dict = {
                "list_resp_" + line_dir: dict_resp_tmp
            }

            table_resp_tmp = {
                "table_data_" + line_dir: table_count
            }
            resp_count = dict(resp_count, **dict_resp_tmp_dict)
            resp_count = dict(resp_count, **table_resp_tmp)



    resp = {
        "msg": msg
    }

    resp = dict(resp, **resp_count)

    os.chdir(_work_path)
    return HttpResponse(json.dumps(resp), content_type="application/json")


@csrf_exempt
def post_xf_stat(request):
    print(request.POST.get('rjxf_id'))
    print(request.POST.get('rjxf_stat'))
    rjxf_id = request.POST.get('rjxf_id')
    # print(config.objects.all())
    #flow_data = flow.objects.filter(**{'rjxf_id': rjxf_id})
    flow_data = flow.objects.get(rjxf_id=rjxf_id)
    flow_data.rjxf_stat = request.POST.get('rjxf_stat')
    flow_data.update_date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    print(flow_data.rjxf_stat)
    flow_data.save()
    resp = {}
    return HttpResponse(json.dumps(resp), content_type="application/json")

@csrf_exempt
def post_chk_stat(request):
    print(request.POST.get('rjxf_id'))
    print(request.POST.get('rjxf_stat'))
    rjxf_id = request.POST.get('rjxf_id')
    # print(config.objects.all())
    #flow_data = flow.objects.filter(**{'rjxf_id': rjxf_id})
    flow_data = flow.objects.get(rjxf_id=rjxf_id)
    flow_data.chk_stat = request.POST.get('chk_stat')
    print(flow_data.chk_stat)
    flow_data.save()
    resp = {}
    return HttpResponse(json.dumps(resp), content_type="application/json")


def check_rjxf_chk_passwd(passwd):
    if passwd == _chk_passwd:
        return True
    else:
        return False

@csrf_exempt
def post_chk_passwd(request):
    print('index post_chk_passwd start')
    print(request.POST.get('rjxf_id'))
    # print(request.POST.get('chk_passwd'))

    code = 0
    msg = '复核成功'
    print(len(request.POST.get('chk_oper')))
    if len(request.POST.get('chk_oper')) < 2:
        msg = '请输入复核人中文名称，谢谢'
        code = -1
    if check_rjxf_chk_passwd(request.POST.get('chk_passwd')) == False:
        msg = '密码校验失败！！！'
        code = -1

    rjxf_id = request.POST.get('rjxf_id')
    flow_data = flow.objects.get(rjxf_id=rjxf_id)
    flow_data.make_chk_oper = request.POST.get('chk_oper')
    if code == 0 : flow_data.save()


    resp = {
        'code': code
        , 'msg': msg
    }
    return HttpResponse(json.dumps(resp), content_type="application/json")

@csrf_exempt
def post_get_tree_list(request):
    input_data = json.loads(request.POST.get("data"))
    list_all_dict_data.clear()
    list_all_dict(input_data)
    resp = {
        "data": list_all_dict_data
    }
    return HttpResponse(json.dumps(resp), content_type="application/json")



