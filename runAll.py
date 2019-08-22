#coding=utf-8
import os
import common.HTMLTestRunner as HTMLTestRunner
import getpathInfo
import unittest
import readConfig
from common.configEmail import send_email
# https://www.cnblogs.com/jfl-xx/p/7717800.html
#pip install apscheduler  apscheduler是python中的任务定时模块，它包含四个组件：触发器（trigger），作业存储（job store），执行器（executor），调度器（scheduler）.
from apscheduler.schedulers.blocking import BlockingScheduler
import pythoncom

send_email = send_email()
path = getpathInfo.get_Path()
report_path = os.path.join(path,'result')
on_off = readConfig.ReadConfig().get_email("on_off")

class AllTest:
    def __init__(self):
        global resultPath
        resultPath = os.path.join(report_path,"report.html")
        #配置执行哪些测试文件的配置文件路径
        self.caseListFile = os.path.join(path,"caselist.txt")
        self.caseFile = os.path.join(path,"testCase")   #真正的断言文件路径
        print("self.caseFile:%s"%self.caseFile)
        self.caseList = []
        
    def set_case_list(self):
        '''
                    读取caselist.txt问件中的用例名称，并添加到caselist元素组
        :return:
        '''
        fb = open(self.caseListFile)
#         fb = open("E:\eclipse\workspace\InterfaceTest_copy\caselist.txt")
        for value in fb.readlines():
            data = str(value)
            if data != '' and not data.startswith("#"):  # 如果data非空且不以#开头
                self.caseList.append(data.replace("\n", ""))    #读取每行数据会将换行转换为\n，去掉每行数据中的\n
                # self.caseList.append(data)
        fb.close()
        
    def set_case_suite(self):
        self.set_case_list() #通过set_case_list()拿到caselist元素组
        test_suite = unittest.TestSuite()
        suite_module = []
        print(self.caseList)
        for case in self.caseList: #从caselist元素组中循环取出case
            case_name = case.split("/")[-1] #通过split函数来将aaa/bbb分割字符串，-1取后面，0取前面
            print(case_name+".py")
            print (case_name)
            discover = unittest.defaultTestLoader.discover(self.caseFile, pattern=(case_name+'.py'),top_level_dir=None)
#             discover = unittest.defaultTestLoader.discover(self.caseFile, pattern='*.py', top_level_dir=None)
            suite_module.append(discover)   #将discover中取出test_name，使用addTest添加到测试集
            print('suite_module:'+str(suite_module))
            if len(suite_module)>0: #判断suite_module元素组是否存在元素
                for suite in suite_module:  #如果存在，循环取出元素组内容，命名为suite
                    for test_name in suite: #从discover中取出test_name，使用addTest添加到测试集
                        test_suite.addTest(test_name)
            else:
                print('else:')
                return None
            return test_suite   #返回测试集
    
    def run(self):
        try:
            suit = self.set_case_suite()    #调用set_case_suite获取test_suite
            print('try')
            print(str(suit))
            if suit is not None:
                print("if-suit")
                fp1 = open(resultPath,'wb')  #打开result/20181108/report.html测试报告文件，如果不存在就创建
                runner = HTMLTestRunner.HTMLTestRunner(stream=fp1,title="测试报告",description="description")
                runner.run(suit)
            else:
                print("Have no case to test.")
        except Exception as ex:
            print(str(ex))
        
        finally:
            print("***********Test END***************")
            fp1.close()
            
        if on_off == 'on':
            send_email.outlook()
        else:
            print("邮件发送开关配置关闭，请打开开关后可正常自动发送测试报告")

if __name__=="__main__":
    AllTest().run()
        
            
        
        
        
        
           