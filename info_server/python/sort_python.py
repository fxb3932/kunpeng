pathList = ['./cs/', './so/', './sql/', './cs12345/', './cs22334']
print(pathList)

def pathSort(pathList, par):
    tmp_list = []
    for line in pathList:
        if line == par:
            tmp_list.insert(0, line)
        else:
            tmp_list.append(line)
    return tmp_list

resp = pathSort(pathList, './cs/')
resp = pathSort(resp, './sql/')
resp = pathSort(resp, './so/')

print(resp)

#字典排序

a = [
    {'a': 1}
    , {'a': 3}
    , {'a': 2}
]
a.sort(key=lambda item: item.get('a'), reverse=True)
print(a)
