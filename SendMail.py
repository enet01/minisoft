#coding:utf-8
import smtplib
from email.mime.text import MIMEText

SMTPserver = 'smtp.sina.com'
sender = 'qkk_space@sina.com'
password = "qkkspace39"
receivers = ['136503868@qq.com','940788158@qq.com']

message = '测试哈 群发！'
msg=[]
msg['Subject'] = '测试哈群发'
msg['From'] = sender
msg['To'] = "136503868@qq.com"

try:
    mailserver = smtplib.SMTP(SMTPserver, 25)
  #  mailserver = smtplib.SMTP()
   # mailserver.connect(SMTPserver, 25)
    mailserver.login(sender, password)


    mailserver.sendmail(sender, receivers, msg.as_string())
except smtplib.SMTPException:
    print("Error: 无法发送邮件")
mailserver.quit()
print('send email success')