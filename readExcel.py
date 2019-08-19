#coding=utf-8
import os
#自己定义的内部类，该类返回项目的绝对路径
import getpathInfo
from xlrd import open_workbook

#拿到该项目所在的绝对路径
path = getpathInfo.get_Path()

class readExcel():
    def get_xls(self,xls_name,sheet_name):
        cls = []
        #获取用例文件路径
        xlspath = os.path.join(path,"testFile","case",xls_name)
        file = open_workbook(xlspath)   #打开用例Excel
        sheet = file.sheet_by_name(sheet_name)      #获得打开Excel的sheet
        
        #获取这个sheet内容行数
        nrows = sheet.nrows
#         print(nrows)
        for i in range(nrows):  #根据行数做循环
            #如果这个Excel的这个sheet的第i行的第一列不等于case_name那么我们把这行的数据添加到cls[]
            if sheet.row_values(i)[0] != u'case_name':
                cls.append(sheet.row_values(i))
        return cls
        
if __name__=="__main__":
    # 测试
    print(readExcel().get_xls('userCase.xlsx', 'login'))
    print(readExcel().get_xls("userCase.xlsx", "login")[0][1])
    print(readExcel().get_xls("userCase.xlsx", "login")[1][2])