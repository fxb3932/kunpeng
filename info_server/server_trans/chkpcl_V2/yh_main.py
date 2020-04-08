#-*- coding: utf-8 *-


import subprocess

class Shell(object):
    def runCmd(self, cmd):
        # cmd = cmd.encode('utf-8')
        print('run_cmd:' + cmd)
        res = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        sout, serr = res.communicate()
        return res.returncode, sout, serr, res.pid

    def getKey(self, cmd, ip, port):
        res = subprocess.Popen('~/bin/zabbix_get -s "' + ip + '" -p' + port + ' -k"' + cmd + '"', shell=True,
                               stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        sout, serr = res.communicate()
        return res.returncode, sout, serr, res.pid
        # print("返回码：" + result[0])
        # print("标准输出：" + result[1])
        # print("标准错误：" + result[2])

class Get(object):
    def keyValue(self, key, date):
        resp_code='ERR'
        try:
            result = shell.getKey('check[run_command:user:./gdxy/' + key + ':hostname:' + date + ']',
                                  line.split(':')[4], line.split(':')[8].rstrip('\n'))
            if result[1].decode('gbk').find('RETURN:OK') != -1:
                resp_code = 'OK'
            else:
                resp_code = 'ERR'
        except:
            resp_code = 'ERR'
        return resp_code


