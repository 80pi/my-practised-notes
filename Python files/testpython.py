import mysql.connector
i,n,c=int(input("enter id")),input("name"),int(input("cclass"))
print(i,n,c)
mydb=mysql.connector.connect(host="127.0.0.1",user="root",passwd="root",database="pythondb",auth_plugin="mysql_native_password")
mycur=mydb.cursor()
mycur.execute("select * from stu")
#mycur.execute("insert into stu values(3,'gopo',4),(5,'bhar',29)")
#mycur.execute("select * from stu")
for i in mycur:
    print(i)
