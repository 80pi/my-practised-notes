
f1=open("D:\\test\\test.txt",'r')
try:
    f=open("D:\\test\\wri.txt","x")
except:
    f=open("D:\\test\\wri.txt","a")
i=1
for x in f1:
  f.write(str(i)+"."+x)
  i+=1
f.close()
f=open("D:\\test\\wri.txt","r")
print(f.read())

