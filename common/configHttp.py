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
        
        # 因为这里要封装post方法，所以这里的url和data值不能写死,参数必须按照url、data顺序传入
        result = requests.post(url=url,data=data).json()
#         result = requests.post(url=url,json=data).json()
        res = json.dumps(result, ensure_ascii=False,sort_keys=True,indent=2)
        return res
    
    def send_get(self,url,data):
        result = requests.get(url=url,params=data).json()
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
    para='name=xiaoming&pwd=111'
    data_payload={"name":"xiaoming","pwd":"111"}
    data_json=json.dumps(data_payload)
#     result = RunMain().run_main('get', 'http://127.0.0.1:9999/login',para)
#     result = RunMain().run_main('post', 'http://127.0.0.1:9999/login',data_payload)
    result = RunMain().run_main('post', 'http://127.0.0.1:9999/login',data_payload)
    
    print(result)

    # post发送请求数据的两种格式：data和json
    payload = {"yoyo":"hello",u"python QQ群":"226296743"}
    # 将payload转换为json格式
    data_json=json.dumps(payload)
    # post data格式
    # r = requests.post("http://httpbin.org/post",data=payload)

    # post json格式
    r =requests.post("http://httpbin.org/post",json=data_json)
    
        
    
    
    
    