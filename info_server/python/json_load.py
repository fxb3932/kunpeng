# /home/insp_ap/software/nginx/html/fxb/jk/system_server/json/ALL.20191114
import json

#    if ( _resp_code < 100 ) return '状态未知';
#    if ( _resp_code === 100 ) return '未开始';
#    if ( _resp_code === 200 ) return '成功';
#    if ( _resp_code === 300 ) return '进行中';
#    if ( _resp_code === 400 ) return '异常';
# 日间步骤  检查9202   特殊批处理 计提增值税 开通9119 损益结转 批处理结束 批后处理
# rjbz     check9202 tspcl     jtzzs    open9119 syjz    pcljs     phcl

f = open("/home/insp_ap/software/nginx/html/fxb/jk/system_server/json/ALL.20191114", encoding='utf-8')
setting = json.load(f)
print(setting)
for line in setting:
    print(line)
    print(line.get('name'))