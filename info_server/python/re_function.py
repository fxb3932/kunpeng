import re
print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.match('com', 'www.runoob.com'))         # 不在起始位置匹配


print(re.match('cs', 'cs12345').span())

print('----------')
resp = []
try:
    resp = re.match('./cs[1-9]\d*/$', './cs12345/').span()
    print(resp[1])

except:
    resp.append('err')
    resp.append(0)
print(resp[1])



print('带大小写忽略的替换')
string_info = "ABC abc Abc aBc"

capital_python = re.findall('abc', string_info, flags=re.IGNORECASE)
sub_result = re.sub('abc', 'bcd', string_info, flags=re.IGNORECASE)

print(capital_python)
print(sub_result)