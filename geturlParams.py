#coding=utf-8
import readConfig as readConfig

readConfig = readConfig.ReadConfig()

class geturlParams():
    def get_url(self):
        new_url = readConfig.get_http('scheme')+"://"+readConfig.get_http('baseurl')+':9999'+'/login'+'?'
        return new_url

if __name__=="__main__":
    print(geturlParams().get_url())