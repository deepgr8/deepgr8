from email import header
import smtplib
import ssl
from ssl import SSLContext
import pandas as pd
from email.mime.multipart import MIMEMultipart  
from email.mime.text import MIMEText
from email.message import EmailMessage




print("press 1 for yahoo mail server \npress 2 for att.net mail server \npress 3 for aol.com mail server \npress 4 for Sbcglobal.net mail server ")
option = int(input("enter your choice from above given options : "))

def yahoo():
    if option==1:
        print("You are using yahoo mail server")
        file=pd.read_excel(str(input("Enter your filename and press enter (for example = filename.xlsx:)")))
        email_column=file.get("email")
        list_of_emails=list(email_column)
        emailid=str(input("Enter your email and press enter: "))
        password=str(input("Enter your password and press enter : "))
        server=smtplib.SMTP("smtp.mail.yahoo.com", 465)
        server.ehlo()
        server.starttls()
        
        server.login(emailid,password)
        
        message=MIMEMultipart()
        sendersname=str(input("Enter senders name : "))
        to=list_of_emails 
        c=","  
                                                  
        message["From"]= sendersname + f"<{emailid}>"
        message["to"]=header.Header(c.join(to))
        message["Subject"]=str(input("Enter your subject :"))
        message["Bcc"]=""
        html_='new work'
        part2=MIMEText(html_,'plain')
        message.attach(part2)
        server.sendmail(emailid,to,message.as_string())
        print(
                "email send successful"
        )
yahoo()        

def att():
    if option==2:
        print("You are using Att.net mail server")
        file=pd.read_excel(str(input("enter your filename with extension (for example = filename.xlsx:)")))
        email_column=file.get("email")
        list_of_emails=list(email_column)
        server=smtplib.SMTP("smtp.mail.yahoo.com",465)
        email_id=str(input("enter your email id :"))
        password=str(input("enter your password: "))
        server.starttls()
        server.login(email_id,password)
        to="deepakprajapati200325@gmail.com"
        # list_of_emails
        print("login successful")
        message=MIMEMultipart('alternatives')
        message['Subject']=str(input("type your subject:- "))
        Sender_name= str(input("Type senders name :"))
        message['From']=Sender_name +f"<{email_id}>"
        # c=',' 
        message["To"] = to
        # header.Header(c.join(to))    
        html_= 'new work'
        part2=MIMEText(html_,'html')
        message.attach(part2)
        server.sendmail(email_id,to,message.as_string())
        print("email sent")
att()


def aol():
    if option==3:
        print("You are using aol.com mail sever")
        # file=pd.read_excel(str(input("enter your filename with extension (for example = filename.xlsx:)")))
        # email_column=file.get("email")
        # # list_of_emails=list(email_column)
        SSLContext=ssl.create_default_context()
        server=smtplib.SMTP_SSL("smtp.aol.com",465,context=SSLContext)
        email_id=str(input("enter your email id :"))
        password=str(input("enter your password: "))
        
        # server.ehlo()
        server.login(email_id,password)
        to="deepakprajapati200325@gmail.com"
        # list_of_emails
        print("login successful")
        message=MIMEMultipart('alternatives')
        message['Subject']=str(input("type your subject:- "))
        Sender_name= str(input("Type senders name :"))
        message['From']=Sender_name +f"<{email_id}>"
        # c=',' 
        message["To"] =to
        # header.Header(c.join(to))    
        html_= 'new work'
        part2=MIMEText(html_,'plain')
        message.attach(part2)
        server.sendmail(email_id,to,message.as_string())
        print("email sent")
aol()

def sbc():
    if option==4:
        print("You are using Sbcglobal.net mail server")

        file=pd.read_excel(str(input("enter your filename with extension (for example = filename.xlsx:)")))
        email_column=file.get("email")
        list_of_emails=list(email_column)
        server=smtplib.SMTP("smtp.mail.att.net",465)
        email_id=str(input("enter your email id :"))
        password=str(input("enter your password: "))
        server.starttls()
        server.login(email_id,password)
        to="deepakprajapati200325@gmail.comm"
        # list_of_emails
        print("login successful")
        message=MIMEMultipart('alternatives')
        message['Subject']=str(input("type your subject:- "))
        Sender_name= str(input("Type senders name :"))
        message['From']=Sender_name +f"<{email_id}>"
        # c=',' 
        message["To"] =to
        # header.Header(c.join(to))    
        html_= 'new work'
        part2=MIMEText(html_,'plain')
        message.attach(part2)
        server.sendmail(email_id,to,message.as_string())
        print("email sent")
sbc()

        