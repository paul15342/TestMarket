#-*- coding:utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
#def send_mail(content,sub):
smtpsever='smtp.163.com'
email='xionghl15342@163.com'
password='x880823'


sendfile=open('D:\\DeskTop\\789.txt','rb').read()

#构造附件
att=MIMEText(sendfile,'base64','utf-8')
att["Content-Type"] = 'application/octet-stream'
att["Content-Disposition"] = 'attachment;  filename="789.txt"'
att['from']='xionghl15342@163.com'
att["to"]='15814663160@163.com'

msgRoot=MIMEMultipart('related')
msgRoot['Subject'] = 'wo shi zhong guo ren'
msgRoot['from']='xionghl15342@163.com'
msgRoot["to"]='15814663160@163.com'
msgRoot.attach(att)

try:
    smtp=smtplib.SMTP()
    smtp.connect(smtpsever)
    smtp.login(email,password)
    smtp.sendmail('xionghl15342@163.com','15814663160@163.com',msgRoot.as_string())
    smtp.quit()
    print 'txt has been sent'
except Exception ,e:
    print (e)
