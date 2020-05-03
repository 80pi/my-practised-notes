import smtplib
import random
senders_email="gopivenkataajay5771@gmail.com"
reveicers_email="9966gopi@gmail.com"
password=input("please enter password")


server=smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login(senders_email,password)
print("successfully logining")
code=random.randrange(1000,9999)
message=("test mail by running python program "+ str(code))
server.sendmail(senders_email,reveicers_email,message)
print("mail succesfully send and a otp is send enter otp for verification")

i=1
while(i):
    verify=int(input("enter code sen to mail"))
    if(verify==code):
        print("mail is verified")
        i=0
    else:
        print("wrong number")
server.quit()
