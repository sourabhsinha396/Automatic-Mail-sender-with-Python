# -*- coding: utf-8 -*-
"""
Created on Fri May 24 15:39:04 2019

@author: Sourabh
"""



import pandas as pd
s=" "
with open ('Hr.txt','r') as file:
    s=file.read().replace('\n',' ')
    



import re  

    
print("Thewhole string is")
print(s,type(s))
    
s=re.sub(r'[^a-zA-Z0-9_.@-]',' ',s)
list_of_emails = re.findall('\S+@\S+', s) 

print(list_of_emails) 
type(list_of_emails)
    

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders



email_user='sourabhsinha396@gmail.com'
# email_send='sourabhsinha693@gmail.com'
subject="Almost done"


msg=MIMEMultipart()
msg['From']=email_user
#msg['To']=email_send
msg['Subject']=subject

body="This is being automatically sent"
msg.attach(MIMEText(body,'plain'))

filename='love.jpg'
attachment=open(filename,'rb')
part=MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= "+filename)

msg.attach(part)
text=msg.as_string()
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email_user,"DemoPass")

#for item in list_of_emails:
    #server.sendmail(email_user,item,text)

server.quit()

