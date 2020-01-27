import smtplib
from email.mime.text import MIMEText
from email.header import Header

#发送html 格式的邮件

#发送邮件
sender = "1075218828@qq.com"
#接受邮箱
receiver = "xuekai20080901@163.com"
#发送邮件主题
subject = "自动化测试"
#发送邮箱服务器
smtpserver = "smtp.qq.com"
#发送邮箱用户名/密码
#username="22132913@qq.com"
#password = "siygipkprzcebjdb"
username = "1075218828@qq.com"
password = "xuekai!QAZ3edc"

#HTML形式的邮件

msg=MIMEText("<html><h1>This Test Report!</h1></html>","html","utf-8")
msg["Subject"]=Header(subject,"utf-8")

smtp=smtplib.SMTP_SSL(smtpserver,465)
smtp.login(username,password)
smtp.sendmail(sender,receiver,msg.as_string())
smtp.quit()