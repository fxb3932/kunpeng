
import datetime
atime = datetime.datetime.strptime('2020-03-25 00:00:00',"%Y-%m-%d %H:%M:%S")
btime = datetime.datetime.strptime('2020-03-25 01:00:00',"%Y-%m-%d %H:%M:%S")
ctime = btime - atime
print(atime)
print(btime)
print(ctime.total_seconds())


a = '2020-03-03 16:22:18 钟勇 18979778117<18979778117@189.cn>'
print(a.split(' '))
print(a.split(' ')[-1])