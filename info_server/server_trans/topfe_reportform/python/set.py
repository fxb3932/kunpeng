set_data = set([])

set_data.add('aml_server')
set_data.add('v2_cib')

print(type(set_data))
if 'aml_server' in set_data:
    print('1')

if 'aml_server' not in set_data:
    print('2')

if 'xxx' not in set_data:
    print('3')

print(set_data)