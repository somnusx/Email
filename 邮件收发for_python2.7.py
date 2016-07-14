#python27
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



#读取邮件
read=poplib.POP3('pop.sina.com')
read.user('somnus_sx@sina.com')#这里设置登陆账号
read.pass_('156csvcsxcs132')#这里设置登陆密码
tongji=read.stat()#这里返回的是邮件基本统计信息
#print tongli #返回两个参数，第一为邮件数， 第二为总字节数
str=read.top(tongji[0],0)#服务器将返回由参数标识的邮件前0行内容，最后str为一个列表，有三个元素
#print str #返回3个参数，[1]对我们有用
str2=[]
for x in str[1]:#其中str中的第二个参数为第一封邮件的各种信息，在这里要给其进行编码
    try:
        str2.append(x.decode())
    except:
        try:
            str2.append(x.decode('gbk'))
        except:
            str2.append((x.decode('big5')))
msg=email.message_from_string('\n'.join(str2))#这个方法能把String的邮件转换成email.message实例
    #msg是把经过编码的str2转化为可识别的邮件信息，并且每行一个信息，join用来连接字符串
biaoti=decode_header(msg['subject'])
if biaoti[0][1]:#如果有第二个元素，说明有编码信息biaoti==[('test',None)]或者biaoti==[('test','utf-8')]
    biaoti2=biaoti[0][0].decode(biaoti[0][1])
else:
    biaoti2=biaoti[0][0]
print (biaoti2)

