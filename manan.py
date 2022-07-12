import random as r #To create random otp importing rand 
import smtplib  # To send mail importing smtplib 

print("Welcome to Zomato")
print("Please verify you crendtials to Login Zomato")
user = input("Enter Your Name   : ") #Enter name
email = input("Enter Your Email : ") # Enter email to verify login
otp = "" # Declaring empty string to store otp
for i in range(6): # for loop for creating a 6 digit otp 
    otp+=str(r.randint(1,9))   # pushing randing number 1 to 9 in string otp
message = (f"Dear {user}, Your OTP to login in Zomato {otp}") # msg that will be displayed to user in mail
s = smtplib.SMTP('smtp.gmail.com', 587) # create a session encapsulate an SMTP connection, port 587 (port number for gmail)
s.starttls() #TLS (Transport Layer Security) encrypts all the SMTP commands when started on s
s.login("mllenahih@gmail.com","vdqzfohghnaihzxi") # Login with official account to mail the otp 

s.sendmail('&&&&&&&&&&&', email, message) # Sending mail to user that contains msg with otp
print("Otp Sent!") # msg after otp is sent
newotp = input("Enter OTP : ") # Enter Otp
if(newotp == otp): # if entered correct otp
     print("OTP Verified")
     order = ["",] # creating list to store the orders
     numberoforders = int(input("Enter Number of orders You want to give :")) # Number of things user need to have
     for i in range(numberoforders): # for loop to get the things
          if(i==0):
              order[i] = input("Name the dish you want to have : ") # taking first order input
          if(i>0):
              ord= input("Name the dish you want to have : ") # taking rest orders as input
              order.insert(i,ord) # inserting at the end and updating the list
     message = (f"Ordered By : {user}\n Order Details : {order}") 
     print(message) # printing order details
else :
    print("Wrong OTP !!!!") # if user enters wront otp exit the program
