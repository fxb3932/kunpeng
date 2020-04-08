import sys
# sys.path.append('../')

import sys

import yh_main as main



shell = main.Shell()
result=shell.runCmd("/sbin/ifconfig -a")
a=result[0]
b=result[1]
c=result[2]
d=result[3]
print(b)
for line in str(b).split('\n'):
    print(line)


print(shell.runCmd('ls /home/insp_ap/devops/info_server/static/app/cloud_file')[1].decode('utf-8'))
# print(shell.getKey('check[run_command:sdf:cat:/cib/kyxjc/rpt/28/7064001_20191128229.rpt]','163.7.64.1','10066')[1].decode('gbk'))

msg=shell.getKey('check[run_command:sdf:cat:/cib/kyxjc/rpt/28/7064001_20191128229.rpt]','163.7.64.1','10066')[1].decode('gbk')
# print(msg)

for line in msg.strip('\n').split('\n'):
    # print(line)
    check_sys=line.split('|')

    if str(check_sys[6]) == "chkpcl":
        #print("-------------------")
        print(check_sys)
    #
    # if check_sys == "Chk__informix_db":
    #     print(line)


msg=":RETURN:AAAA:END:a:b:"
print(msg.lstrip("RETURN:"))
print(msg.lstrip("RETURN:").rstrip(":END"))
print(msg.strip("a:"))


theString = 'saaaay yes no yaaaass'
print(theString.lstrip('say'))
