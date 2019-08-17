#coding=utf-8

import os

def get_Path():
    # 将path分割成目录和文件名二元组返回。
#     print os.path.split("/getpathInfo.py")
    path = os.path.split(os.path.realpath(__file__))[0]
    
    return path

if __name__=="__main__":
    print ('测试路径是否OK，路径为：'+get_Path())