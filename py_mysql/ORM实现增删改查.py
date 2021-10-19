#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# In[10]:


connect = create_engine("mysql+pymysql://root:011022@localhost:3306/work",
                        encoding="utf-8",
                        echo=True)
Base = declarative_base()


# In[11]:


class Student(Base):
    __tablename__ = 'student'
    Sno = Column(Integer,primary_key=True) # 学号
    Sname = Column(String(20),nullable=False)# 姓名
    Ssex = Column(String(10), nullable=False) # 性别
    Sage = Column(Integer,nullable=False) #年龄
    Sdept = Column(String(20),nullable=False) #系


# In[12]:


# define session
Session = sessionmaker(bind=connect)


# In[25]:


class OrmTest(object):
    def __init__(self):
        self.session = Session()
        
    # 新增记录 
    def add_one(self):
        new_obj = Student(
            Sno = '20210125',
            Sname = '李四',
            Ssex = '男',
            Sage = 18,
            Sdept = 'CS',
        )
        self.session.add(new_obj)
        self.session.commit()
        return new_obj
    
    # 查询一条记录
    def get_one(self):
        return self.session.query(Student).get(1)
    
    def get_more(self):
        return self.session.query(Student).all()


# In[26]:


test = OrmTest()
# test.add_one()
test.get_one()


# In[28]:


Students = test.get_more()


# In[33]:


for i in Students:
    print("Sno is :{},Sname is;{},Ssex is :{},Sage is :{},Sdept is :{}".format(i.Sno,i.Sname,i.Ssex,i.Sage,i.Sdept),end='\n')


# In[ ]:




