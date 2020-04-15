import pymysql



def connect_mysql(sql):
    print('连接 mysql 数据库')
    conn = pymysql.connect(
        host="163.1.6.40"
        , user="root", password="Cibwh1685/",
        database="insp_ap",
        charset="utf8")

    cursor = conn.cursor()

    print('mysql 执行SQL：')
    print(sql)

    cursor.execute(sql)

    data = cursor.fetchall()

    conn.close()

    print('mysql 返回结果：')
    for line in data:
        print(line)
    return data


sql = """
select a.type_id, b.code, b.name, count(*) 
from search_problem_action a, search_problem_action_type b 
where a.oper = '费学彬' 
and a.type_id = b.id
group by a.type_id, b.code, b.name ;
"""
data = connect_mysql(sql)
print(data)
for line in data:
    print(line[2])
