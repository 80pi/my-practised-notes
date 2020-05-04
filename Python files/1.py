import mysql.connector
mydb=mysql.connector.connect(host="127.0.0.1",user="root",passwd="root",database="pythondb",auth_plugin="mysql_native_password")
mycur=mydb.cursor()

'''
#adding new users to db using same id and password if in new create one
username,password=input("enter username "),input("enter password ")
sql="insert into admin(username,password) values(%s,%s)"
val=(username,password)
mycur.execute(sql,val)
mydb.commit()
print("successfully register")
mycur.execute("select * from admin")
for i in mycur:
    print(i)
'''

#login validation
username,password=input("enter username "),input("enter password ")
mycur.execute("select * from admin")
f=0
for i in mycur:
    if(i[0]==username and i[1]==password):
        f=1
        break
if(f==1):
    print("login successfullly")
else:
    print("invalid id and password")
#login validation over


    


