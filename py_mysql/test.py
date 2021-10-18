# coding=gbk
import pymysql
# 使用python连接mysql（测试）

# 连接数据库
conn = pymysql.connect(host='localhost',user='root',password='011022',database='work',port=3306)
# 获取游标对象
cursor = conn.cursor()

# 查询所有数据
cursor.execute("select * from student")



result = cursor.fetchall()
# 查看查询结果
print(result)