import pymysql.cursors

# 连接数据库
connection = pymysql.connect(host='163.1.6.40',
                             user='root',
                             password='Cibwh1685/',
                             db='insp_ap',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
try:
    with connection.cursor() as cursor:
        # 读取单条记录
        sql = "SELECT distinct bank_name from trans_dlwl_chnltrans;"
        cursor.execute(sql)
        result = cursor.fetchall()
        for line in result:
            print(line.get('bank_name'))
finally:
    connection.close()