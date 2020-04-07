def show():
    return {"stat":True, "txt": 'bbb'}

print(show().get('stat'))
print(show().get('txt'))
print(show().get('resp'))