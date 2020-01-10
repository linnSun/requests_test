# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# ProjectName:     Test0805
# FileName:       RequestMethod 
# Author:        MuTou
# Date:         2019/10/16
# Description:
#-------------------------------------------------------------------------------
#声明一个全局变量进行标记请求后的文本是何种类型；默认True的话则表示文本是json格式
#如果是false则非json格式
import requests
class Request_Method:
    def __init__(self):
        self.FlagType=True
    def  get_or_post(self,method,url,data,cookies=None):
        if method=="GET":
           return requests.get(url,params=data,cookies=cookies)
        elif method=="POST":
           return  requests.post(url,data=data,cookies=cookies)

    #声明一个方法获取进行获取执行结果后的实际结果;实际测试肯定希望获取json格式的数据
    def  get_respone_actual(self,method,url,data,cookies=None):
        #获取到响应对象
        try:
            self.FlagType=True
            return self.get_or_post(method,url,data,cookies=cookies).json()
        except:
            self.FlagType=False
            return self.get_or_post(method,url,data,cookies=cookies).text




    #声明一个方法：返回响应的cookie
    def  get_respone_cookie(self,method,url,data):
        return self.get_or_post(method,url,data).cookies









