#coding=utf-8
import unittest
import getpathInfo
import os

class test(unittest.TestCase):
    
    def test01(self):
        self.caseList=['user/test01case']
        self.test_suite = unittest.TestSuite()
        self.suite_module = []
        self.path = getpathInfo.get_Path()
        self.caseFile = os.path.join(self.path,"testCase") 
        for case in self.caseList: #从caselist元素组中循环取出case
            case_name = case.split("/")[-1] #通过split函数来将aaa/bbb分割字符串，-1取后面，0取前面
            print(case_name+".py")
            discover = unittest.defaultTestLoader.discover(self.caseFile, pattern=(case_name+'.py'), top_level_dir=None)
                # discover = unittest.defaultTestLoader.discover(self.caseFile, pattern='*.py', top_level_dir=None)
           
            self.suite_module.append(discover)   #将discover中取出test_name，使用addTest添加到测试集
            print('suite_module:'+str(self.suite_module))
            if len(self.suite_module)>0: #判断suite_module元素组是否存在元素
                for suite in self.suite_module:  #如果存在，循环取出元素组内容，命名为suite
                    for test_name in suite: #从discover中取出test_name，使用addTest添加到测试集
                        self.test_suite.addTest(test_name)  
            else:
                print('else:')
                return None
            return self.test_suite   #返回测试集
        
        
        
if __name__=="__main__":
    unittest.main()
        
    