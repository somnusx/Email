#python24
#电子邮件的操作
import poplib
import smtplib
from email.header import decode_header
from email.mime.text import MIMEText


#如何登陆邮箱
#按目的分为是为发送邮件而登陆还是为读取邮件而登陆
#先说为发送邮件而登陆的操作
sent=smtplib.SMTP('smtp.sina.com')#这一行设置了SMTP服务器为smtp.sina.com
sent.login('somnus_sx@sina.com','156csvcsxcs132')


#发送邮件
#刚才我们已经登陆，现在需要设置发送内容，然后发送即
to=['somnus_sx@sina.com','1459853598@qq.com']#发送到两个邮箱里这就是群发功能
content=MIMEText('How do you do?')#也就是说，MIMEText的参数代表邮件的具体内容
content['Subject']='test'#这里设置了邮件标题
content['From']='somnus_sx@sina.com'#这里设置了邮件从哪里发送
content['To']=','.join(to)#这里设置了邮件要发送的地址，可以群发
sent.sendmail('somnus_sx@sina.com',to,content.as_string())#这一步实现发送邮件，有三个参数
sent.close()
