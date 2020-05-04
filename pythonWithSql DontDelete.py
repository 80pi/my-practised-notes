import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="pythonsqlpractise",auth_plugin="mysql_native_password")
cur=mydb.cursor()
# to create db
# cur.execute("create database test2")

# to see database
# cur.execute("show databases")

# to drop database
# cur.execute("drop database test2")

# to create table
# cur.execute("create table stu(id int,name varchar(20),age int)")

# to see tables
# cur.execute("show tables")

# to drop tables
# cur.execute("drop table stu")

# to add columns
# cur.execute("alter table stu add(gender varchar(1))")

# to drop columns
# cur.execute("alter table stu drop column gender")
# or
# cur.execute("alter table stu drop gender")

# to modify datatype
# cur.execute("alter table stu modify gender varchar(6)")

# to modify table name
# cur.execute("alter table student rename stu")

# to modify column
# cur.execute("alter table stu rename column gender to gen")

# to drop table
# cur.execute("drop table stu")

# to insert data into table # while insertion commit need to done as databasename.commit()
# stmt="insert into stu(id,name,age,gender) values(%s,%s,%s,%s)"
# val=(6,"xcv",26,"m")
# cur.execute(stmt,val)
# mydb.commit()
# print(cur.rowcount)   # tells us that how many no of rows were inserted in to db


# # to multiple records insert data into table # while insertion commit need to done as databasename.commit()
# stmt="insert into stu(id,name,age,gender) values(%s,%s,%s,%s)"
# val=[
# (3,"def",21,"m"),
# (4,"efg",23,"f"),
# (4,"fgh",24,"m"),
# (5,"ghj",25,"f")
# ]
# cur.executemany(stmt,val)
# mydb.commit()
# print(cur.rowcount)

# select stmt
# stmt="select * from stu"
# cur.execute(stmt)
# rr=cur.fetchall()
# for i in rr:
#     print(i)

# select only first column by where condition
# stmt="select * from stu"
# val=(3,)
# cur.execute(stmt,val)
# rr=cur.fetchone()
# for i in rr:
#     print(i)

#select only on condition
# stmt="select * from stu where id=%s"
# val=(3,)#if string "3",
# cur.execute(stmt,val)
# rr=cur.fetchall()
# for i in rr:
#     print(i)

# # order by desc
# stmt="select * from stu order by age desc"
# cur.execute(stmt)
# rr=cur.fetchall()
# for i in rr:
#     print(i)

# # order by asc
# stmt="select * from stu order by age"
# cur.execute(stmt)
# rr=cur.fetchall()
# for i in rr:
#     print(i)

# delete on condition # if no cndtion just(cur.execute("delete  from stu"))
# stmt="delete  from stu where age=%s"
# val=(25,) # if string means ("gopi",)
# cur.execute(stmt,val)

# updating
# stmt="update stu set name=%s where id=%s"
# val=("gajay",1,)
# cur.execute(stmt,val)

# # limit
# cur.execute("select * from stu limit 3")
# rr=cur.fetchall()
# for i in rr:
#     print(i)

# limit with offset just like(skip in mongodb)
# cur.execute("select * from stu limit 3 offset 2")
# rr=cur.fetchall()
# for i in rr:
#     print(i)


# raw structure of table
# id int      name strig    age int     gender stirng
