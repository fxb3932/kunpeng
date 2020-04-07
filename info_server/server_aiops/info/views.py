from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    print('start index')

    # 权限检查
    auth_data = {
        'request': request
        , 'net': False
        , 'login': False
        , 'debug': True
        , 'perm': ''
    }
    resp_auth = main.auth(auth_data)
    if resp_auth.get('code') == False:
        return render(request, 'alarm/resp.html', {"message": resp_auth.get('msg')})
    # s_date = time.strftime('%Y-%m-%d', time.localtime())
    # # input = 'topfe_server'
    # # f = open('/home/insp_ap/inspect/src/switch/' + input + '/config.ini', 'r', encoding='gbk')
    # list_req = []
    # resp = shell.getKey('check[run_command:user:./trans_search/get_bank_info.sh]', _ip, _port)
    # try:
    #     myview = resp[1].decode('GBK').split('\n')
    # except:
    #     myview = resp[1]
    #
    # for line_info in myview:
    #     if line_info.startswith('RETURN:') == True:
    #         list_req.append({'bank_id': line_info.split(':')[1].strip()})
    #
    #
    # # for line in f.readlines():
    # #     line = line.rstrip('\n')
    # #     if line.startswith('#') != True:
    # #         # print(line.split(':')[1] + '_' + line.split(':')[0])
    # #         list_req.append({'bank_id': line.split(':')[1], 'bank_name': line.split(':')[0]})
    #
    # # print(list_req)
    # req = {
    #     'title': '代理支付交易查询',
    #     'date': s_date,
    #     'req': list_req
    # }
    # # print(req)
    # return render(request, 'myview/index.html', req)
    return render(request, 'info/index.html')


import os
import json
import sys
import cx_Oracle
from django.views.decorators.csrf import csrf_exempt  # 可post调用url

sys.path.append('/home/insp_ap/software/nginx/html/myview/src/views/myview/report')
import main


@csrf_exempt
def get(request):
    print('start get')
    os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.ZHS16GBK'
    os.environ['ORACLE_HOME'] = '/oracle/orasoft/product/11.2.0/dbhome_1'
    data = []
    conn = cx_Oracle.connect(main.getConnInfo())
    cursor = conn.cursor()
    sql = "select * from myview_info_data t order by recid desc"
    cursor.execute(sql)

    i = 0

    def ProcKey(a):
        if f[a] == None:
            return ''
        else:
            return f[a].strip()

    for f in cursor.fetchall():
        data.append({
            'recid': f[0],
            'text': ProcKey(1),
            'proc': ProcKey(2),
            'username': ProcKey(3),
            'tel': ProcKey(4),
            'mail': ProcKey(5),
            'input': ProcKey(6),
            'setdate': ProcKey(7)
        })

    cursor.close()
    conn.close()
    return HttpResponse(json.dumps(data), content_type="application/json")


@csrf_exempt
def post(request):
    print('start post')
    os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.ZHS16GBK'
    os.environ['ORACLE_HOME'] = '/oracle/orasoft/product/11.2.0/dbhome_1'
    # req = json.loads(sys.argv[1])
    # req = sys.argv[1]
    print(request.POST.get('recid'))
    print(request.POST)

    # httpResp = "保存成功，感谢您对知识库的完善：）"

    auth_data = {
        'request': request
        # , 'net_sc': True
        , 'login': True
        , 'debug': False
        , 'perm': ''
    }
    resp_auth = main.auth(auth_data)
    if resp_auth.get('code') == False:
        resp = {"msg": '风险控制，生产环境不得保存信息，请谅解：）'}
        return HttpResponse(json.dumps(resp), content_type="application/json")

    def UpdateKey(a, b):
        if a in request.POST:
            print("ok")
        try:
            if request.POST.get(a) == '':
                print('UpdateKey try row ' + a + ':' + str(b))
                return row.get(b)
            else:
                print('UpdateKey except req ' + a + ':' + str(b))
                return request.POST.get(a).replace('\xa0', ' ').replace('\u202c', ' ')
                # return request.POST.get(a)
        except:
            print('UpdateKey except ' + a + ':' + str(b))
            return ''

    def runsql(input_cursor, input_sql, input_data):
        try:
            input_cursor.execute(input_sql, input_data)
            conn.commit()
            input_cursor.close()
            return "保存成功，感谢您对知识库的完善：）"
        except cx_Oracle.DatabaseError as msg:
            return '处理方式目前最大内容长度为：3000字节</br>' + str(msg)
        except UnicodeEncodeError as msg:
            return '检测到异常的字符，请联系开发人员处理</br>' + str(msg)
        cursor.close()

    conn = cx_Oracle.connect(main.getConnInfo())
    cursor = conn.cursor()


    if request.POST.get('recid') == '0':
        print('insert data')
        insert_cursor = conn.cursor()
        sql = 'insert into MYVIEW_INFO_DATA(recid,text,proc,username,tel,mail,input,setdate) values(seq_info.nextval,:text,:proc,:username,:tel,:mail,:input,:setdate)'
        data = {
            "text": request.POST.get('text'),
            "proc": request.POST.get('proc').replace('\xa0', ' '),
            "username": request.POST.get('username'),
            "tel": request.POST.get('tel'),
            "mail": request.POST.get('mail'),
            "input": request.POST.get('input'),
            "setdate": request.POST.get('setdate')
        }
        httpResp = runsql(insert_cursor, sql, data)
    else:
        sql = 'select * from myview_info_data where recid = ' + request.POST.get('recid')
        cursor.execute(sql)
        row = cursor.fetchone()
        print('update recid ' + str(row[0]))

        update_cursor = conn.cursor()
        sql = 'update MYVIEW_INFO_DATA set text=:text, proc=:proc, username=:username, tel=:tel, mail=:mail, input=:input, setdate=:setdate where recid = ' + str(
            row[0])
        print(sql)
        data = {
            "text": UpdateKey('text', 1),
            "proc": UpdateKey('proc', 2),
            "username": UpdateKey('username', 3),
            "tel": UpdateKey('tel', 4),
            "mail": UpdateKey('mail', 5),
            "input": UpdateKey('input', 6),
            "setdate": UpdateKey('setdate', 7)
        }
        print(data)
        # update_cursor.execute(sql, data)
        httpResp = runsql(update_cursor, sql, data)

    print('msg = [' + str(httpResp) + ']')
    return HttpResponse(json.dumps({"msg": str(httpResp)}), content_type="application/json")


def test(request):
    return render(request, 'info/test.html')
