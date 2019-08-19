#coding=utf-8

'''
Created on 2019年8月19日

@author: Administrator
'''

import requests
import json

class RunMain():
    '''
    classdocs
    '''


    def send_post(self,url,data):
        '''
        Constructor
        '''
        # 因为这里要封装post方法，所以这里的url和data值不能写死,参数必须按照url、data顺序传入
        result = requests.post(url=url,data=data).json()
        
        res = json.dumps(result, ensure_ascii=False,sort_keys=True,indent=2)
        return res
    
    def send_get(self,url,data):
        result = requests.get(url=url,data=data)
        res = json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)
        return res
    
    def run_main(self,method,url=None,data=None):
        result = None
        if method=='post':
            result=self.send_post(url, data)
        elif method=='get':
            result=self.send_get(url, data)
        else:
            print("method值错误！！！")
        return result
    
if __name__=="__main__":
    # 写死参数，进行测试
    result = RunMain().run_main('post', 'http://127.0.0.1:9999/login','name=xiaoming&pwd=111')
    print(result)
    
    
    
    
    