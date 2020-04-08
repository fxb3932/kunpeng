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