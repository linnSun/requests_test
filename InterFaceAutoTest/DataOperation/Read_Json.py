# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# ProjectName:     Test0805
# FileName:       Read_Json 
# Author:        MuTou
# Date:         2019/10/16
# Description:
#-------------------------------------------------------------------------------
import json
class ReadJson:
    def __init__(self,jsonPath):
        #获取读取json数据的对象
        with open(jsonPath,"r",encoding="utf-8") as fp:
            self.get_json_object=json.load(fp)
    # def  get_result(self):
    #     print(type(self.get_json_object))
    def get_excelkey_value(self,key):
        try:
            return self.get_json_object[key]
        except:
            return None


if __name__ == '__main__':
    jj=ReadJson("./ParameterData.json")






