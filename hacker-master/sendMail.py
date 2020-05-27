import smtplib
from email.mime.text import MIMEText
user=''
pwd=''
def sendMail(user,pwd,to,subject,text):
    msg=MIMEText(text)
    msg['From']=user
    msg['To']=to
    msg['Subject']=subject
    try:
        smtpServer=smtplib.SMTP('smtp.gmail.com',587)
        print('[+] Connetcting To Mail Server')
        smtpServer.ehlo()
        print('[+] Starting Encrypted Session')
        smtpServer.starttls()
        #smtpServer.ehlo()
        print('[+] Logging Into Mail Server')
        smtpServer.login(user,pwd)
        print('[+] Sending Mail')
        smtpServer.sendmail(user,to,msg.as_string())
        smtpServer.close()
        print('[+] Mail Send Successfully')
    except Exception as e:
        print(e)
        print('[-] Sending Mail Failed')


sendMail(user,pwd,'44698055@qq.com','Re:Important','Test Message111')
