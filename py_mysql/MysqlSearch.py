# coding=gbk
import pymysql


class MysqlSearch():
    # 初始化
    def __init__(self):
        self.get_conn()

    def get_conn(self):
        # 连接数据库
        self.conn = pymysql.connect(host='localhost', user='root', password='011022', database='work', port=3306)

    def close_conn(self):
        try:
            if self.conn:
                # 关闭连接
                self.conn.close()
        except:
            print("关闭异常")

    # 获取一条数据
    def get_one(self):
        # 准备sql
        sql = "select * from student"
        # 获取cursor(游标对象)
        cursor = self.conn.cursor()
        # 执行sql
        cursor.execute(sql)
        # print(cursor.description)  # 查看字段名称以及其他数据
        # 拿到数据
        result = cursor.fetchone()
        # print(result)
        # 处理数据
        # print(result[0]) #获取第一个数据（测试处理数据）
        result = dict(zip([k[0] for k in cursor.description],cursor.fetchone())) # 将数据转成字典类型
        print(result)
        # 关闭cursor/连接
        cursor.close()
        self.close_conn()

    # 获取一条数据
    def get_more(self):
        # 准备sql
        sql = "select * from student"
        # 获取cursor(游标对象)
        cursor = self.conn.cursor()
        # 执行sql
        cursor.execute(sql)
        # print(cursor.description)  # 查看字段名称以及其他数据
        # 拿到数据
        # result = cursor.fetchone()
        # print(result)
        # 处理数据
        # print(result[0]) #获取第一个数据（测试处理数据）
        result = [dict(zip([k[0] for k in cursor.description],row))
                  for row in cursor.fetchall()] # 将数据转成字典类型
        print(result)
        # 关闭cursor/连接
        cursor.close()
        self.close_conn()


    # 添加一条数据
    def add_one(self):
        # 准备sql
        sql = ("insert into student values(%s,%s,%s,%s,%s);")
        # 获取cursor（游标对象）
        cursor = self.conn.cursor()
        # 执行sql
        cursor.execute(sql,('20211019',"张三",'男','19','IS'))
        # 提交数据到数据库
        #提交事务
        self.conn.commit()
        # 关闭cursor和连接
        cursor.close()
        self.close_conn()


