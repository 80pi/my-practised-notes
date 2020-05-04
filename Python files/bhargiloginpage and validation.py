import mysql.connector

#adding new users to db using same id and password if in new create one
def addnewuserbyold():
    rusername,rpassword=input("enter refereence admin string username "),input("enter refereence admin string password ")
    r=uservalid(rusername,rpassword)
    if(r==1):
        username,password=input("enter username "),input("enter password ")
        sql="insert into admin(username,password) values(%s,%s)"
        val=(username,password)
        mydb=mysql.connector.connect(host="127.0.0.1",user="root",passwd="root",database="pythondb",auth_plugin="mysql_native_password")
        mycur=mydb.cursor()
        mycur.execute(sql,val)
        mydb.commit()
        print("successfully register")
        
def seeallusers():
    mydb=mysql.connector.connect(host="127.0.0.1",user="root",passwd="root",database="pythondb",auth_plugin="mysql_native_password")
    mycur=mydb.cursor()
    mycur.execute("select * from admin")
    for i in mycur:
       print(i)


#login validation
def uservalid(rusername,rpassword):
    #username,password=input("enter username "),input("enter password ")
    mydb=mysql.connector.connect(host="127.0.0.1",user="root",passwd="root",database="pythondb",auth_plugin="mysql_native_password")
    mycur=mydb.cursor()
    mycur.execute("select * from admin")
    f=0
    for i in mycur:
        if(i[0]==rusername and i[1]==rpassword):
            f=1
            break
    if(f==1):
        print("login successfullly")
        return 1
    else:
        print("invalid id and password")
        return 0
    #login validation pow
addnewuserbyold()
seeallusers()

    


