# coding=gbk
import pymysql
# ʹ��python����mysql�����ԣ�

# �������ݿ�
conn = pymysql.connect(host='localhost',user='root',password='011022',database='work',port=3306)
# ��ȡ�α����
cursor = conn.cursor()

# ��ѯ��������
cursor.execute("select * from student")



result = cursor.fetchall()
# �鿴��ѯ���
print(result)