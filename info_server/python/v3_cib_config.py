import configparser

conf = configparser.ConfigParser()
conf.read('/home/insp_ap/inspect/src/switch/v3_cib/run/trans_mon/discovery.ini', encoding='gbk')
# print("所有节点==>", conf.sections())

f = open('/home/insp_ap/inspect/src/switch/v3_cib/config.ini.cmdb', 'r', encoding='gbk')
file_data = f.readlines()

suc_flag = True
config_data_list = []
config_data_list_err = []
for line in conf.sections():
    i = 0
    for file_line in file_data:
        file_line = file_line.rstrip('\n')
        if file_line.startswith(conf.get(line, 'bank_group')):
            # ['天津农商行', 'TJNSH', 'cib', 'AIX', '163.7.75.1', 'XXX', '第五批', '村镇', '10066', 'kyx_perV1']
            _line_2 = file_line.split(':')[2]
            _line_3 = file_line.split(':')[3]
            _line_4 = file_line.split(':')[4]
            _line_5 = file_line.split(':')[5]
            _line_6 = file_line.split(':')[6]
            _line_7 = file_line.split(':')[7]
            _line_8 = file_line.split(':')[8]
            _line_9 = file_line.split(':')[9]
            i += 1

    if conf.get(line, 'bank_group') == '瑞金光大':
        patch = 'V3_CIB_RJGD'
    else:
        patch = 'v3plus'
    #print(i)
    if i != 1:
        suc_flag = False
        config_data_list_err.append(conf.get(line, 'bank_group'))
    config_data = conf.get(line, 'bank_name') \
                  + ':' + conf.get(line, 'bank_id') \
                  + ':' + _line_2 \
                  + ':' + _line_3 \
                  + ':' + _line_4 \
                  + ':' + _line_5 \
                  + ':' + line \
                  + ':' + _line_7 \
                  + ':' + _line_8 \
                  + ':' + _line_9 \
                  + ':' + patch
    config_data_list.append(config_data)

if suc_flag is True:
    for line in config_data_list: print(line)
else:
    print('config error :')
    for line in config_data_list_err : print(line)
