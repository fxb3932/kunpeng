import cx_Oracle
import os
import sys


os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.ZHS16GBK'
os.environ['ORACLE_HOME'] = '/oracle/orasoft/product/11.2.0/dbhome_1'

# conn = cx_Oracle.connect(main.getConnInfo())
# cursor = conn.cursor()
# sql = "select * from myview_info_data t order by recid desc"
# cursor.execute(sql)


conn = cx_Oracle.connect('insp_ap/insp_ap@163.1.6.40:1521/orcl')  # 用自己的实际数据库用户名、密码、主机ip地址 替换即可

cursor = conn.cursor()
date1="20200318000000"
date2="20200318230000"

sql = '''
select * from (
select info.hostname,info.keyname,dbms_lob.substr(histext.value, 2000),count(*) as detail from history_text histext,
    (SELECT a.name as groupname ,c.hostid as hostid,c.host ,c.name as hostname,d.ip as ip,d.port as port ,e.itemid as itemid,e.name as keyname,e.key_ as key_ from hstgrp A
           JOIN hosts_groups B ON A.GROUPID=B.GROUPID
           JOIN hosts C on C.HOSTID = B.HOSTID
           join interface D on b.hostid=d.hostid
           join items E on e.hostid in c.hostid
    where  e.key_ like 'trans_errtxt[%' or e.key_ like 'trans_err[%'
    ) info
where histext.itemid in info.itemid
   and histext.clock > timetoint(to_date('''+date1+''', 'yyyymmddhh24miss'))
   and histext.clock < timetoint(to_date('''+date2+''', 'yyyymmddhh24miss'))
group by info.hostname, info.keyname, dbms_lob.substr(histext.value, 2000)
order by count(*) desc
) where rownum <11
'''
# cursor.execute(sql)
# for f in cursor.fetchall():
#     print(f)
# cursor.close()
# conn.close()


#######################################################################
date1="20200318000000"
date2="20200318230000"
print("--------------------------------------------------------------")
conn = cx_Oracle.connect('insp_ap/insp_ap@163.1.6.40:1521/orcl')
cursor = conn.cursor()
sql = '''
select * from (
select trigger_info.hostname,trigger_info.ip,event.name,trigger_info.triggerid,event.severity,count(*)  from events event,
(
SELECT distinct a.name as groupname,c.hostid as hostid,c.host ,c.name as hostname,d.ip as ip,d.port as port ,t.triggerid as triggerid ,t.description as description from hstgrp A
           JOIN hosts_groups B ON A.GROUPID=B.GROUPID
           JOIN hosts C on C.HOSTID = B.HOSTID
           join interface D on b.hostid=d.hostid
           join items E on e.hostid in c.hostid
           join functions f on f.itemid=e.itemid
           join  triggers t on t.triggerid =f.triggerid
    --where a.name='V3核心系统_10066' --and e.key_ like '%trans%' and t.description like '%闵行%'
    --where c.name ='CKXT40_CKXT_查控系统40_查控系统'
) trigger_info
where event.severity >='1'
    and clock >= timetoint(to_date('''+date1+''', 'yyyymmddhh24miss'))
    and clock <= timetoint(to_date('''+date2+''', 'yyyymmddhh24miss'))
    and event.objectid=trigger_info.triggerid
    and event.source='0'
    and event.object='0'
group by trigger_info.hostname,trigger_info.ip,event.name,trigger_info.triggerid,event.severity
order by  count(*) desc)
where rownum <100
'''
cursor.execute(sql)
for f in cursor.fetchall():
    print(f)
cursor.close()
conn.close()
