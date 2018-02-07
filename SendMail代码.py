#coding:utf-8
import smtplib
from email.mime.text import MIMEText

receiver=['2247615761@qq.com']
username="shizhongjain01@sina.com"
password="854945urusei"

subject='this is a test email from python'
msg=MIMEText('这是测试文件','plain','utf-8')
# msg['Subject']=Header(subject,'utf-8')
msg['Subject']=subject
# msg['from'] = username
msg['for'] = username
msg['To']=receiver[0]

smtp=smtplib.SMTP()
smtp.connect('smtp.sina.com',25)
smtp.login(username,password)
smtp.sendmail(username,receiver,msg.as_string())
print("mail is send success")
smtp.quit

print ("done")
