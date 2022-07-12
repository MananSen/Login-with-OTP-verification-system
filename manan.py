import random as r
import smtplib

print("Welcome to Zomato")
print("Please verify you crendtials to Login Zomato")
user = input("Enter Your Name   : ")
email = input("Enter Your Email : ")
otp = ""
for i in range(6):
    otp+=str(r.randint(1,9))   
message = (f"Dear {user}, Your OTP to login in Zomato {otp}")
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("mllenahih@gmail.com","vdqzfohghnaihzxi")
s.sendmail('&&&&&&&&&&&', email, message)
print("Otp Sent!")
newotp = input("Enter OTP : ")
if(newotp == otp):
     print("OTP Verified")
     order = ["",]
     numberoforders = int(input("Enter Number of orders You want to give :"))
     for i in range(numberoforders):
          if(i==0):
              order[i] = input("Name the dish you want to have : ")
          if(i>0):
              ord= input("Name the dish you want to have : ")
              order.insert(i,ord)
     message = (f"Ordered By : {user}\n Order Details : {order}")
     print(message)