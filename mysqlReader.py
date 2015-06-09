# encoding: utf-8
#!/usr/bin/python

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect(db='mybigdata',host='localhost',user='kong',passwd='kong')
print db
# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# 使用execute方法执行SQL语句
cursor.execute("SET NAMES utf8")
# cursor.execute("SET CHARACTER_SET_CLIENT=utf8")
# cursor.execute("SET CHARACTER_SET_RESULTS=utf8")
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取一条数据库。
data = cursor.fetchone()

print "Database version : %s " % data

# # SQL 插入语句
# sql = """INSERT INTO table1(id,
#          name)
#          VALUES ('', '北京人')"""
# try:
#    # 执行sql语句
#    cursor.execute(sql)
#    # 提交到数据库执行
#    db.commit()
# except:
#    print "Excute error"
#    # Rollback in case there is any error
#    db.rollback()



# SQL 查询语句
sql = "SELECT * FROM table1 order by id asc"

try:
   # 执行SQL语句
   cursor.execute(sql)
   # 获取所有记录列表
   results = cursor.fetchall()
   
   list1 = []
   for row in results:
      ids = row[0]
      name = row[1]
      # print ids,name
      temp = str(name)+str(ids)
      #temp = temp.decode('utf-8')  
      print temp
      
      # 这个地方显示\xe5\xb1\xb1\xe4\xb8\x9c\xe4\xba\xba2'
      list1.append(temp)

      
      
      # 打印结果
      # print "id=%s,lname=%s" % \
      #        (id, name )
   print list1
except:
   print "Error: unable to fecth data"





# 关闭数据库连接
db.close()