# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 10:29:35 2019

@author:Sourabh Sinha
"""


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders



email_user='sourabhsinha@gmail.com'
email_send='smmehtaTPO@gmail.com'
subject="Python sending mail with sub+attachment"


msg=MIMEMultipart()
msg['From']=email_user
msg['To']=email_send
msg['Subject']=subject

body="Hi there Abhijeet ,Its me using python to send mail"
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
server.login(email_user,"Demo_Password")



server.sendmail(email_user,email_send,text)
server.quit()

