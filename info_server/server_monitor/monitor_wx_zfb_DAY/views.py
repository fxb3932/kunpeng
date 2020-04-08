from django.shortcuts import render
from django.http import HttpResponse
import pymysql.cursors
import time


def get_CurDate():
    CurDate = time.strftime("%Y%m%d", time.localtime())
    CurDate="20191212"
    return CurDate


def get_MysqlConfig():
    MySqlConnect = pymysql.connect(host='163.1.6.40',
                                   user='root',
                                   password='Cibwh1685/',
                                   db='insp_ap',
                                   charset='utf8mb4',
                                   cursorclass=pymysql.cursors.DictCursor)
    return MySqlConnect


# Create your views here.
def index(request):
    req = {}
    test = 'aaa'
    print(test)
    return render(request, 'monitor_wx_zfb/index.html', req)


def monitor(request):
    req = {}
    test = 'aaa'
    print(test)
    return render(request, 'monitor11/index.html', req)

def picCvt(request):
    req = {}
    test = 'aaa'
    print(test)
    return render(request, 'monitor_wx_zfb/picCvt.html', req)


import json
import pymysql.cursors
from django.views.decorators.csrf import csrf_exempt  # 可post调用url


@csrf_exempt
# 获取交易总量计时数据
def get_M1_TransTot(request):
    print('start post')
    print(request.POST)  # form 包含提交的数据
    print(request.POST.get('start'))

    connection = get_MysqlConfig()
    try:
        with connection.cursor() as cursor:
            # 读取单条记录
            sql = '''
            select a.now ,b.ago from
(select sum(trans_count_all)  as now from monitor_wx_zfb_trans_flow where settle_date='20191212'
and txn_time < '2019-12-12 23:59:59') a,
(
select sum(trans_count_all) as ago from monitor_wx_zfb_trans_flow where settle_date='20191212'
and txn_time < '2019-12-12 23:59:59')  b;      
            '''
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result[0])
            # for line in result:
            #     #print(line.get('bank_name'))
            #     list.append(line.get('bank_name'))
    finally:
        connection.close()

    resp = {
        "startcount": "100",
        "endcount": "1000"
    }
    resp = {
        "startcount": result[0].get('ago'),
        "endcount": result[0].get('now')
    }
    resp = {
        "startcount": 364245,
        "endcount": 364245
    }
    return HttpResponse(json.dumps(resp), content_type="application/json")


@csrf_exempt
# 获取每分钟根据业务类型分布数据
def get_L1_TransChnlMin_BAK(request):
    print('start post')
    print(request.POST)  # form 包含提交的数据
    print(request.POST.get('start'))
    print("aaaaaaaaaa")
    sCurDate = get_CurDate()

    time_list = []
    wx_list = []
    zfb_list = []
    other_list = []
    # 从mysql中获取数据

    list = []

    # 连接数据库
    connection = get_MysqlConfig()
    try:
        with connection.cursor() as cursor:
            # 读取单条记录
            # curDate = '20191016'
            sql = '''
            select date_format(txn_time,'%H:%i') as hz_time ,hz_tran_type,sum(trans_count_all) as hz_tot from
(
    select  *,
    case when trans_type='财付通' then '微信'
    when trans_type='支付宝' then '支付宝'
    else '其他' END 'hz_tran_type'
    from monitor_wx_zfb_trans_flow
    where settle_date=''' + sCurDate + '''
    and txn_time > date_sub(now(),interval 120 minute)
) m
group by date_format(txn_time,'%H:%i'),hz_tran_type order by 1;
            '''
            print(sql)
            cursor.execute(sql);
            result = cursor.fetchall();

            for line in result:
                time_list.append(line.get('hz_time'))
            # 通过集合去重
            set_time = sorted(set(time_list), key=time_list.index)

            for tran_time in set_time:
                wx_data = 0;
                zfb_data = 0;
                other_data = 0;
                for line2 in result:
                    if line2.get('hz_time') == tran_time:
                        if line2.get('hz_tran_type') == '微信':
                            wx_data = line2.get('hz_tot')
                        if line2.get('hz_tran_type') == '支付宝':
                            zfb_data = line2.get('hz_tot')
                        if line2.get('hz_tran_type') == '其他':
                            other_data = line2.get('hz_tot')
                    else:
                        continue
                wx_list.append(wx_data)
                zfb_list.append(zfb_data)
                other_list.append(other_data)
    finally:
        connection.close()

    resp = {
        "time": set_time,
        "wx_data": wx_list,
        "zfb_data": zfb_list,
        "other_data": other_list,
    }
    # resp = {
    #     "startcount": result[0].get('ago'),
    #     "endcount": result[0].get('now')
    # }
    print("-----------------------------------------------------------")
    for msg in resp:
        print(str(msg) + ":" + str(len(resp.get(msg))))
    print(resp)
    print("-----------------------------------------------------------")
    return HttpResponse(json.dumps(resp), content_type="application/json")


@csrf_exempt
# 获取每分钟根据业务类型分布数据
def get_L1_TransChnlMin(request):
    print('start post')
    print(request.POST)  # form 包含提交的数据
    print(request.POST.get('start'))
    print("aaaaaaaaaa")
    sCurDate = get_CurDate()

    time_list = []
    wx_list = []
    zfb_list = []
    other_list = []
    # 从mysql中获取数据

    list = []

    # 连接数据库
    connection = get_MysqlConfig()
    try:
        with connection.cursor() as cursor:
            # 读取单条记录
            # curDate = '20191016'
            sql = '''
                        select date_format(txn_time,'%H:%i') as hz_time ,hz_tran_type,sum(trans_count_all) as hz_tot from
            (
                select  *,
                case when trans_type='财付通' then '微信'
                when trans_type='支付宝' then '支付宝'
                else '其他' END 'hz_tran_type'
                from monitor_wx_zfb_trans_flow
                where settle_date=''' + sCurDate + '''
                and txn_time > '2019-12-12 22:00:00'
            ) m
            group by date_format(txn_time,'%H:%i'),hz_tran_type order by 1;
                        '''
            print(sql)
            cursor.execute(sql);
            result = cursor.fetchall();

            for line in result:
                time_list.append(line.get('hz_time'))
            # 通过集合去重
            set_time = sorted(set(time_list), key=time_list.index)

            for tran_time in set_time:
                wx_data = 0;
                zfb_data = 0;
                other_data = 0;
                for line2 in result:
                    if line2.get('hz_time') == tran_time:
                        if line2.get('hz_tran_type') == '微信':
                            wx_data = line2.get('hz_tot')
                        if line2.get('hz_tran_type') == '支付宝':
                            zfb_data = line2.get('hz_tot')
                        if line2.get('hz_tran_type') == '其他':
                            other_data = line2.get('hz_tot')
                    else:
                        continue
                wx_list.append(wx_data)
                zfb_list.append(zfb_data)
                other_list.append(other_data)
    finally:
        connection.close()

    resp = {
        "time": set_time,
        "wx_data": wx_list,
        "zfb_data": zfb_list,
        "other_data": other_list,
    }
    # resp = {
    #     "startcount": result[0].get('ago'),
    #     "endcount": result[0].get('now')
    # }
    print("------------------------L1-----------------------------------")
    for msg in resp:
        print(str(msg) + ":" + str(len(resp.get(msg))))
    print(resp)
    print("-------------------------L1----------------------------------")
    return HttpResponse(json.dumps(resp), content_type="application/json")


@csrf_exempt
# 获取一周的交易量数据
def get_L2_TransWeek(request):
    print('start post')
    print(request.POST)  # form 包含提交的数据
    print(request.POST.get('start'))
    week_list = []
    week_tot = []

    # 连接数据库
    connection = get_MysqlConfig()
    try:
        with connection.cursor() as cursor:
            # 读取单条记录
            sql = '''
            select settle_date,sum(trans_count_all) as week_tot from monitor_wx_zfb_trans_flow
where settle_date >  '20191205' AND SETTLE_DATE <'20191213'
group by settle_date
order by settle_date;
            '''
            cursor.execute(sql);
            result = cursor.fetchall();
            # print(result)
            # print(result[0])
            for line in result:
                week_list.append(line.get('settle_date'))
                week_tot.append(line.get('week_tot'))
    finally:
        connection.close()

    resp = {
        "week_list": week_list,
        "week_tot": week_tot,
    }
    print("------------------------L2-----------------------------------")
    print(resp)
    print("------------------------L2-----------------------------------")
    return HttpResponse(json.dumps(resp), content_type="application/json")


@csrf_exempt
# 获取每分钟根据业务类型分布数据
def get_L3_TransDayType(request):
    print('start post')
    print(request.POST)  # form 包含提交的数据
    print(request.POST.get('start'))
    print("aaaaaaaaaa")

    date_list = []
    date_wx_list = []
    date_zfb_list = []
    date_other_list = []
    date_tot_list = []

    # 连接数据库
    connection = get_MysqlConfig()
    try:
        with connection.cursor() as cursor:
            # 读取单条记录

            sql = '''
select settle_date as settle_date ,hz_tran_type,sum(trans_count_all) as hz_tot from
(
    select  *,
    case when trans_type='财付通' then '微信'
    when trans_type='支付宝' then '支付宝'
    else '其他' END 'hz_tran_type'
    from monitor_wx_zfb_trans_flow
    where settle_date >='20191206' AND settle_date <='20191212'
) m
group by settle_date,hz_tran_type order by 1;
            '''
            cursor.execute(sql);
            result = cursor.fetchall();
            print("----------------------------------------------")
            print(result)
            print("----------------------------------------------")
            # print(result[0])
            for line in result:
                date_list.append(line.get('settle_date'))
                if line.get('hz_tran_type') == '微信':
                    date_wx_list.append(line.get('hz_tot'))
                if line.get('hz_tran_type') == '支付宝':
                    date_zfb_list.append(line.get('hz_tot'))
                if line.get('hz_tran_type') == '其他':
                    date_other_list.append(line.get('hz_tot'))
                else:
                    date_other_list.append(0)

            # 通过集合去重
            set_settle_date = sorted(set(date_list), key=date_list.index)
            # print(set_time)
            # print(wx_list)
            # print(zfb_list)
            # print(other_list)
            for i in range(0, len(set_settle_date)):
                tot_tmp = 0
                tot_tmp = date_wx_list[i] + date_zfb_list[i] + date_other_list[i]
                date_tot_list.append(tot_tmp)
    finally:
        connection.close()

    resp = {
        "settle_date": set_settle_date,
        "date_wx_list": date_wx_list,
        "date_zfb_list": date_zfb_list,
        "date_other_list": date_other_list,
        "date_tot_list": date_tot_list,
    }
    # resp = {
    #     "startcount": result[0].get('ago'),
    #     "endcount": result[0].get('now')
    # }
    print("------------------------L3-----------------------------------")
    print(resp)
    print("------------------------L3-----------------------------------")
    return HttpResponse(json.dumps(resp), content_type="application/json")





@csrf_exempt
# right1 获取邯郸和代理网联交易明细
def get_R1_TransPlatRate_BAK(request):
    connection = get_MysqlConfig()
    sCurDate = get_CurDate()
    try:
        with connection.cursor() as cursor:
            # 读取单条记录

            sql = '''
                select date_format(txn_time,'%H:%i') as hz_time ,hz_tran_plat,sum(trans_count_all) as hz_tot,
                sum(trans_count_err) as hz_err_tot
                from
                (
                    select  *,
                    case when bank_ch_name='邯郸银行' then '邯郸网联'
                    else '兴业网联' END 'hz_tran_plat'
                    from monitor_wx_zfb_trans_flow
                    where settle_date=''' + sCurDate + '''
                    and txn_time > date_sub(now(),interval 120 minute)

                ) m
                group by date_format(txn_time,'%H:%i'),hz_tran_plat order by 1;
            '''




            # date_sub(now(),interval 120 minute)
            cursor.execute(sql);
            result = cursor.fetchall();

            xywl_list = [];
            hdwl_list = [];
            time_list = [];
            rate_list = [];

            for line in result:
                time_list.append(line.get('hz_time'))
            # 通过集合去重
            set_time = sorted(set(time_list), key=time_list.index)

            for tran_time in set_time:
                hdwl_data = 0;
                hdwl_err_data = 0;
                xywl_data = 0;
                xywl_err_data = 0;
                rate = 0;
                for line2 in result:
                    all_trans_tot = 0;
                    all_err_trans_tot = 0;
                    trans_rate = 0;

                    if line2.get('hz_time') == tran_time:

                        if line2.get('hz_tran_plat') == '邯郸网联':
                            hdwl_data = line2.get('hz_tot')
                            hdwl_err_data = line2.get('hz_err_tot')
                            hdwl_list.append(hdwl_data)
                        if line2.get('hz_tran_plat') == '兴业网联':
                            xywl_data = line2.get('hz_tot')
                            xywl_err_data = line2.get('hz_err_tot')
                            xywl_list.append(xywl_data)

                        all_trans_tot = hdwl_data + xywl_data
                        all_err_trans_tot = hdwl_err_data + xywl_err_data
                        if all_trans_tot == 0:
                            trans_rate = 0;
                        trans_rate = round((1 - all_err_trans_tot / all_trans_tot) * 100, 2)
                        rate_list.append(trans_rate)
                    else:
                        continue

    finally:
        connection.close()

    resp = {
        "time_list": set_time,
        "hdwl_list": hdwl_list,
        "xywl_list": xywl_list,
        "rate_list": rate_list
    }
    print(resp)
    return HttpResponse(json.dumps(resp), content_type="application/json")

@csrf_exempt
# right1 获取邯郸和代理网联交易明细
def get_R1_TransPlatMin(request):
    connection = get_MysqlConfig()
    sCurDate = get_CurDate()
    try:
        with connection.cursor() as cursor:
            # 读取单条记录

            # sql = '''
            #     select date_format(txn_time,'%H:%i') as hz_time ,hz_tran_plat,sum(trans_count_all) as hz_tot,
            #     sum(trans_count_err) as hz_err_tot
            #     from
            #     (
            #         select  *,
            #         case when bank_ch_name='邯郸银行' then '邯郸网联'
            #         else '兴业网联' END 'hz_tran_plat'
            #         from monitor_wx_zfb_trans_flow
            #         where settle_date=''' + sCurDate + '''
            #         and txn_time > '2019-12-12 22:00:00'
            #
            #     ) m
            #     group by date_format(txn_time,'%H:%i'),hz_tran_plat order by 1;
            # '''

            sql = '''
                select date_format(txn_time,'%H:%i') as hz_time ,hz_tran_plat,sum(trans_count_all) as hz_tot,
                sum(trans_count_err) as hz_err_tot
                from
                (
                    select  *,
                    case when bank_ch_name='邯郸银行' then '邯郸网联'
                    else '兴业网联' END 'hz_tran_plat'
                    from monitor_wx_zfb_trans_flow
                    where settle_date='20191212'
                    and txn_time >= '2019-12-12 22:00:00'
                    and txn_time <= '2019-12-12 23:59:59'

                ) m
                group by date_format(txn_time,'%H:%i'),hz_tran_plat order by 1;
            '''


            print('============================================')
            print(sql)
            print('============================================')

            # sql = '''
            #     select date_format(txn_time,'%H:%i') as hz_time ,hz_tran_plat,sum(trans_count_all) as hz_tot,
            #     sum(trans_count_err) as hz_err_tot
            #     from
            #     (
            #         select  *,
            #         case when bank_ch_name='邯郸银行' then '邯郸网联'
            #         else '兴业网联' END 'hz_tran_plat'
            #         from monitor_wx_zfb_trans_flow
            #         where settle_date='20181111'
            #         and txn_time <'2018-11-11 02:00:00'
            #
            #
            #     ) m
            #     group by date_format(txn_time,'%H:%i'),hz_tran_plat order by 1;
            # '''



            # date_sub(now(),interval 120 minute)
            cursor.execute(sql);
            result = cursor.fetchall();

            xywl_list = [];
            hdwl_list = [];
            time_list = [];
            rate_list = [];

            for line in result:
                time_list.append(line.get('hz_time'))
            # 通过集合去重
            set_time = sorted(set(time_list), key=time_list.index)




            for tran_time in set_time:
                hdwl_data = 0;
                hdwl_err_data = 0;
                xywl_data = 0;
                xywl_err_data = 0;
                rate = 0;
                for line2 in result:
                    all_trans_tot = 0;
                    all_err_trans_tot = 0;
                    trans_rate = 0;

                    if line2.get('hz_time') == tran_time:
                        if line2.get('hz_tran_plat') == '邯郸网联':
                            hdwl_data = line2.get('hz_tot')
                            hdwl_err_data = line2.get('hz_err_tot')

                        if line2.get('hz_tran_plat') == '兴业网联':
                            xywl_data = line2.get('hz_tot')
                            xywl_err_data = line2.get('hz_err_tot')



                    else:
                        continue
                all_trans_tot = hdwl_data + xywl_data
                all_err_trans_tot = hdwl_err_data + xywl_err_data
                if all_trans_tot == 0:
                    trans_rate = 0;
                trans_rate = round((1 - all_err_trans_tot / all_trans_tot) * 100, 2)
                hdwl_list.append(hdwl_data)
                xywl_list.append(xywl_data)
                rate_list.append(trans_rate)

    finally:
        connection.close()

    resp = {
        "time_list": set_time,
        "hdwl_list": hdwl_list,
        "xywl_list": xywl_list,
        "rate_list": rate_list
    }
    print("------------------------R1-----------------------------------")
    print(resp)
    return HttpResponse(json.dumps(resp), content_type="application/json")


@csrf_exempt
# 获取TOP10
def get_R5_TransTopHD(request):
    connection = get_MysqlConfig()
    sCurDate = get_CurDate()
    try:
        with connection.cursor() as cursor:
            # 读取单条记录

            sql = '''
select bank_ch_name,sum(trans_count_all) as bank_tot from monitor_wx_zfb_trans_flow where settle_date=''' + sCurDate + '''
and bank_ch_name ='邯郸银行'
group by bank_ch_name
order by 2 desc limit 10;        
            '''
            cursor.execute(sql);
            result = cursor.fetchall();
            print(result)

            list_bank_ch_name = []
            list_bank_tot = []
            for line in result:
                # print(line)
                key_name = line.get('bank_ch_name').strip('市商业银行').strip('村镇银行').strip('山东')
                if key_name == '梅州客':
                    key_name = '梅州客商'
                list_bank_ch_name.append(key_name)
                list_bank_tot.append(line.get('bank_tot'))

    finally:
        connection.close()
    resp = {
        'bank_ch_name': list_bank_ch_name,
        'list_bank_tot': list_bank_tot
    }
    print("------------------------R5-----------------------------------")
    print(resp)
    return HttpResponse(json.dumps(resp), content_type="application/json")
@csrf_exempt
# 获取TOP10
def get_R6_TransTop10(request):
    connection = get_MysqlConfig()
    sCurDate = get_CurDate()
    try:
        with connection.cursor() as cursor:
            # 读取单条记录

            sql = '''
select bank_ch_name,sum(trans_count_all) as bank_tot from monitor_wx_zfb_trans_flow where settle_date=''' + sCurDate + '''
and bank_ch_name !='邯郸银行'
group by bank_ch_name
order by 2 desc limit 10;        
            '''
            cursor.execute(sql);
            result = cursor.fetchall();
            print(result)

            list_bank_ch_name = []
            list_bank_tot = []
            for line in result:
                # print(line)
                key_name = line.get('bank_ch_name').strip('市商业银行').strip('村镇银行').strip('山东')
                if key_name == '梅州客':
                    key_name = '梅州客商'
                list_bank_ch_name.append(key_name)
                list_bank_tot.append(line.get('bank_tot'))

    finally:
        connection.close()
    resp = {
        'bank_ch_name': list_bank_ch_name,
        'list_bank_tot': list_bank_tot
    }
    print("------------------------R6-----------------------------------")
    print(resp)
    return HttpResponse(json.dumps(resp), content_type="application/json")


@csrf_exempt
# 获取双11交易分步
def get_R2_TransComHis(request):
    connection = get_MysqlConfig()
    sCurDate = get_CurDate()
    try:
        with connection.cursor() as cursor:
            # 读取单条记录
            sCurTime = time.strftime("%H:%M:%S", (time.localtime(time.time() - 120)))
            sHisCurTime = '2018-11-11 ' + sCurTime
            sql = '''
            select a.settle_date,sum(a.trans_count_all) as trans_tot,round(sum(a.trans_amt_all),0) as trans_amt from
            (select * from monitor_wx_zfb_trans_flow where settle_date=''' + sCurDate + '''
            union
            select * from monitor_wx_zfb_trans_flow where settle_date='20181111' and txn_time < "'''+sHisCurTime+'''") a
            group by a.settle_date;
                        '''

            print("---------------------------------------------------")
            print("aaa")

            sql = '''
select a.settle_date,sum(a.trans_count_all) as trans_tot,round(sum(a.trans_amt_all),0) as trans_amt from
(select * from monitor_wx_zfb_trans_flow where settle_date=''' + sCurDate + '''
union
select * from monitor_wx_zfb_trans_flow where settle_date='20181111') a
group by a.settle_date;
            '''
            cursor.execute(sql);
            result = cursor.fetchall();
            his_tot = 0
            cur_tot = 0
            his_amt = 0
            cur_amt = 0
            for line in result:
                if (line.get('settle_date') == sCurDate):
                    cur_tot = line.get('trans_tot')
                    cur_amt = line.get('trans_amt')
                else:
                    his_tot = line.get('trans_tot')
                    his_amt = line.get('trans_amt')

    finally:
        connection.close()
    resp = {
        'cur_tot': cur_tot,
        'cur_amt': cur_amt,
        'his_tot': his_tot,
        'his_amt': his_amt
    }
    resp = {
        'cur_tot': 364245,
        'cur_amt': cur_amt,
        'his_tot': his_tot,
        'his_amt': his_amt
    }
    print("------------------------R2-----------------------------------")
    print(resp)
    return HttpResponse(json.dumps(resp), content_type="application/json")


@csrf_exempt
# right1 获取邯郸和代理网联平台交易占比
def get_R4_TransPlatRate(request):
    connection = get_MysqlConfig()
    try:
        with connection.cursor() as cursor:
            # 读取单条记录

            #             sql = '''
            # select m.sys_plat_name,sum(m.trans_count_all) as trans_tot from
            #    (select  *,case when bank_ch_name='邯郸银行' then '兴业邯郸代理网联' else '兴业代理网联' END 'sys_plat_name'
            #      from monitor_wx_zfb_trans_flow
            #    where settle_date=date_format(now(),'%Y%m%d')
            #                 and plat_name='DLWL') m
            # group by m.sys_plat_name;
            #             '''
            sql = '''
            select m.sys_plat_name,sum(m.trans_count_all) as trans_tot from 
               (select  *,case when bank_ch_name='邯郸银行' then '兴业邯郸代理网联' else '兴业代理网联' END 'sys_plat_name'
                 from monitor_wx_zfb_trans_flow
               where txn_time > date_sub(now(), interval 5 minute)
                            and plat_name='DLWL') m
            group by m.sys_plat_name;
                        '''

            cursor.execute(sql);
            result = cursor.fetchall();
            xydlwl_tot = 0
            hddlwl_tot = 0
            for line in result:
                if (line.get('sys_plat_name') == "兴业邯郸代理网联"):
                    hddlwl_tot = line.get('trans_tot')
                elif (line.get('sys_plat_name') == "兴业代理网联"):
                    xydlwl_tot = line.get('trans_tot')
            print("husdfsdjfsjdkfhsk")
            print("aaaaaaaaaaaaaaaaaaaaaaa")
            yh = {
                'name': 'huiyang',
                'age': '30'

            }
            print("bbbbbbbbbbbbbbbbbbbb")
            yh2 = "aaa"
            print("cccccccccccccccccccccc")


    finally:
        connection.close()

    resp = {
        'xydlwl_tot': xydlwl_tot,
        'hddlwl_tot': hddlwl_tot
    }
    print("------------------------R4-----------------------------------")
    print(resp)
    return HttpResponse(json.dumps(resp), content_type="application/json")





@csrf_exempt
# 获取交易金额5分钟内的起始结束值
def get_M2_TransAmt(request):
    connection = get_MysqlConfig()
    try:
        with connection.cursor() as cursor:
            # 读取单条记录

            sql = '''
select a.amt_now ,b.amt_ago from
(select sum(trans_amt_all)/1  as amt_now from monitor_wx_zfb_trans_flow where settle_date='20191212'
and txn_time < '2019-12-12 23:59:59') a,
(
select sum(trans_amt_all)/1 as amt_ago from monitor_wx_zfb_trans_flow where settle_date='20191212'
and txn_time < '2019-12-12 23:59:59')  b;          
            '''
            cursor.execute(sql);
            result = cursor.fetchall();
            print(result)

            for line in result:
                print(list)
    finally:
        connection.close()

    resp = {
        "startcount_amt": result[0].get('amt_ago'),
        "endcount_amt": result[0].get('amt_now')
    }
    # resp = {
    #     "startcount_amt": 12345678900,
    #     "endcount_amt":   34567890111
    # }
    print(resp)
    return HttpResponse(json.dumps(resp), content_type="application/json")


@csrf_exempt
# 返回天微信、支付宝交易占比R3
def get_R3_TransChnlBX(request):
    connection = get_MysqlConfig()
    wx_data = 0
    zfb_data = 0
    other_data = 0
    try:
        with connection.cursor() as cursor:
            # 读取单条记录

            sql = '''
            select a.tran as trans_type,sum(a.trans_count_all) as trans_tot from
(
    select  *,
    case when trans_type='财付通' then '微信'
    when trans_type='支付宝' then '支付宝'
    else '其他' END 'tran'
    from monitor_wx_zfb_trans_flow
    where settle_date='20191212') a
group by a.tran;      
            '''
            cursor.execute(sql);
            result = cursor.fetchall();

            for line in result:
                print("---------------------------")
                print(line)
                print("aaaaaaaaaaaaaaaaaaaaaaaaaaaa")
                print("bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")
                if (line.get('trans_type') == '微信'):
                    wx_data = line.get('trans_tot')
                elif (line.get('trans_type') == '支付宝'):
                    zfb_data = line.get('trans_tot')
                elif (line.get('trans_type') == '其他'):
                    other_data = line.get('trans_tot')
    finally:
        connection.close()

    resp = {
        "wx_data": wx_data,
        "zfb_data": zfb_data,
        "other_data": other_data
    }
    resp = {
        "wx_data": wx_data,
        "zfb_data": 145933,
        "other_data": other_data
    }
    print("------------------------R3-----------------------------------")
    print(resp)
    return HttpResponse(json.dumps(resp), content_type="application/json")


@csrf_exempt
# DEMO
def z_get_post_default(request):
    # 连接数据库
    connection = pymysql.connect(host='163.1.6.40',
                                 user='root',
                                 password='Cibwh1685/',
                                 db='insp_ap',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            sql = '''
            SQL位置       
            '''
            # 执行sql
            cursor.execute(sql);
            result = cursor.fetchall();
            print(result)

            # 取出数据
            for line in result:
                print(list)
    finally:
        # 关闭数据库
        connection.close()

    resp = {
        "data1": 'data1',
        "data2": 'data2'
    }
    return HttpResponse(json.dumps(resp), content_type="application/json")

@csrf_exempt
def get_yh_data(request):


    # http://163.1.6.40:19096/monitor_nzjs/get_data
    # http://163.1.6.40:19092/monitor_nzjs/get_data
    # http://163.1.6.40:19098/monitor_wx_zfb_DAY/get_yh_data
    # http://163.1.6.40:19098/monitor_wx_zfb/get_R1_TransPlatMin

    data = {
        '汇总数据': {
            '已完成百分比': 0.85
            , '进行中百分比': 0.49
            , '失败百分比': 0.2
        }

        , 'aaa':[
            {'x': '测试', 'y': 20}
            , {'x': 2, 'y': 40}
            , {'x': 3, 'y': 50}
            , {'x': 4, 'y': 30}
            , {'x': 5, 'y': 20}
        ]
        , 'bbb':[
            {'name': 'aaa', 'value': 0.30}
            , {'name': 'bbb', 'value': 0.30}

        ]
        ,  'ccc':{
            'time':['aa','nbb'],
            'value':['12','15']
        }
    }
    return HttpResponse(json.dumps(data), content_type="application/json")
