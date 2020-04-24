role_list = [
    {"role_id": 1, "role_name": 'admin', 'authority': 'create_staff'},
    {"role_id": 1, "role_name": 'admin', 'authority': 'delete_staff'},
    {"role_id": 1, "role_name": 'admin', 'authority': 'read_staff'},
    {"role_id": 2, "role_name": 'manager', 'authority': 'read_staff'},
    {"role_id": 2, "role_name": 'manager', 'authority': 'delete_staff'},
    {"role_id": 3, "role_name": 'staff', 'authority': 'read_staff'}
]

for line in role_list:
    print(line)

m = {}
for i in role_list:
    rid, rn = str(i['role_id']), i['role_name']
    print('rid = ' + str(rid))
    print('rn  = ' + str(rn))
    m.setdefault(rid+rn, {
      'role_id': rid,
      'role_name': rn,
      'authority': []
    })['authority'].append(i['authority'])
print(m.values())

for line in m.values():
    print(line)