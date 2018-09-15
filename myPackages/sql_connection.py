import pymysql

# 连接数据库
connect = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='Mysql940208!',
    db='shayxu'
    # charset='utf8'
)

'''
    show databases;
    use xxxx;
    show tables;
'''

cursor = connect.cursor()

sql = "select * from Persons"

cursor.execute(sql)
connect.commit()
print('成功插入', cursor.rowcount, '条数据')
connect.close()






# select * from employees
# where hire_date =
# (select max(hire_date) from employees)

