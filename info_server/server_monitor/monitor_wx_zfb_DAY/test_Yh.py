print("aaaa")


mydict={
    'yingyong':{
        'name':{'hostnme':'aa','lastname':'bb'}
    },
    'xitong':{
        'list':[1,3,4,5,6]
    }

}
zlevel=100
dict = {'Name': 'Zara', 'Age': 7}
dict2 = {'Sex': 'female' }
dict.update(dict2)
print(dict)
list=[{'name':'aaa'},{'name':'bbbb'}]

print("aaa")
msg=10000
print("ddddddddddddddddddddd")

import datetime
import arrow


def getTime(self, flag, dayhourminute):
    '''
    获取几小时之前,几分钟前，几天前，几个月前，及几年前的具体时间 flag, 1:天；2：小时；3：分钟；4：月，5：年
    :param flag: 1:天；2：小时；3：分钟；4：月，5：年
    :param dayhourminute: 整数值
    :return: 具体时间 %Y-%m-%d %H:%M:%S
    '''
    tn = datetime.datetime.now()
    t = None
    ttime = ''
    if flag <= 3:
        if flag == 1:
            t = datetime.timedelta(days=dayhourminute)
        elif flag == 2:
            t = datetime.timedelta(hours=dayhourminute)
        elif flag == 3:
            t = datetime.timedelta(minutes=dayhourminute)
        strtime = tn - t
        ttime = strtime.strftime('%Y-%m-%d %H:%M:%S')
    else:
        dt = arrow.now()
        if flag == 4:
            ttime = dt.shift(months=-dayhourminute).format("YYYY-MM-DD HH:MM:SS")
        elif flag == 5:
            ttime = str(
                int(datetime.datetime.now().strftime("%Y")) - dayhourminute) + "-" + datetime.datetime.now().strftime(
                "%m-%d")
    return ttime
msg=getTime(1,3,3)
print(msg)

import time
curTime=time.strftime("%Y-%m-%d %H:%M:%S", (time.localtime(time.time()-120)))
print(curTime)
t=time.localtime(time.time() - 300)
print(t.tm_year)

sCurTime = time.strftime("%H:%M:%S", (time.localtime(time.time() - 120)))
sHisCurTime = '2018-11-11 ' + sCurTime
print(sHisCurTime)







