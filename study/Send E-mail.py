
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
def send_mail(content,sub):
    smtpsever='smtp.163.com'
    email='xionghl15342@163.com'
    password='x880823'
    msg=MIMEText(content,'plain','utf-8')
    msg['from']='xionghl15342@163.com'
    msg["to"]='15814663160@163.com'
    msg['subject']=sub
    try:
        smtp=smtplib.SMTP()
        smtp.connect(smtpsever)
        smtp.login(email,password)
        smtp.sendmail('xionghl15342@163.com','15814663160@163.com',msg.as_string())
        smtp.quit()
    except Exception ,e:
        print (e)
if __name__=="__main__":
    send_mail('this is python','Python Email')