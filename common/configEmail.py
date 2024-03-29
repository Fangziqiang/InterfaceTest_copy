#coding=utf-8
import os

# pip2 install pywin32com
import win32com.client as win32
import datetime
import readConfig
import getpathInfo

read_conf = readConfig.ReadConfig()
subject = read_conf.get_email('subject')    #从配置文件中读取，邮件主题
app = str(read_conf.get_email('app'))       #从配置文件读取邮件类型
address = read_conf.get_email('addressee')  #从配置文件中读取，邮件收件人
cc = read_conf.get_email('cc')              #读取邮件抄送人
mail_path = os.path.join(getpathInfo.get_Path(),'result','report.html')     # 获取测试报告路径

class send_email():
    def outlook(self):
#         olook = win32.Dispatch("%s.Application"%app)
        olook=win32.gencache.EnsureDispatch('%s.Application'% app)
        mail = olook.CreateItem(win32.constants.olMailItem)
        
        mail.To = address
        mail.CC = cc
        mail.Subject = str(datetime.datetime.now())[0:19]+'%s'%subject
        mail.Attachments.Add(mail_path,1,1,"myFile")
        content = """
            执行测试中......
            测试已完成！！
            生成报告中....
            报告已生成...
            报告已邮件发送!!
            """
        mail.Body = content
        mail.Send()
        
if __name__=="__main__":
    print(subject)
    send_email().outlook()
    print('send email ok!!!!!')