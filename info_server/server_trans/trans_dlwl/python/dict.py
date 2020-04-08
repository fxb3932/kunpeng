import subprocess


class Shell(object):
    def runCmd(self, cmd):
        res = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        sout, serr = res.communicate()
        return res.returncode, sout, serr, res.pid

    def getKey(self, cmd, ip, port):
        res = subprocess.Popen('~/bin/zabbix_get -s "' + ip + '" -p' + port + ' -k"' + cmd + '"', shell=True,
                               stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        print("~/bin/zabbix_get -s " + ip + " -p" + port + "-k" + cmd)
        sout, serr = res.communicate()
        return res.returncode, sout, serr, res.pid
        # print("返回码：" + result[0])
        # print("标准输出：" + result[1])
        # print("标准错误：" + result[2])


dBankInfo = {
    'dlzf_hd': {"name": '兴业银行代理网联', 'ip': '163.51.1.13', 'port': '10066'},
    'dlzf': {"name": '邯郸银行代理网联', 'ip': '163.51.1.14', 'port': '10066'}
}
print(dBankInfo.get('dlzf').get('name'))
shell = Shell();
ip=dBankInfo.get('dlzf').get('ip')
port=dBankInfo.get('dlzf').get('port')
msg = shell.getKey('check[run_command:user:get_dlwl\/get_dlwl.sh]', ip,port)

try:
    info = msg[1].decode('GBK').split('\n')
except:
    info = msg[1]
list=[];
for line in info:
    if line.startswith('RETURN:') == True:
        sBankName=line.split(':')[1]
        #print(sBankName)
        list.append(sBankName)
print(list)

