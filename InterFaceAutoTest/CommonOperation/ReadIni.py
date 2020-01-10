# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# ProjectName:     Test0805
# FileName:       ReadIni 
# Author:        MuTou
# Date:         2019/10/17
# Description:
#-------------------------------------------------------------------------------
import os
import configparser
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
class  Read_Ini:
       def __init__(self):
           get_ini_path=os.path.join(BASE_DIR,"CommonOperation/path_data.ini")
           self.config=configparser.ConfigParser()
           self.config.read(get_ini_path)
           self.section =self.config["path"]
       #获取excel的路径
       def  get_excel_path(self):
           return os.path.join(BASE_DIR,self.section["excel_path"])
       #获取shee_name
       def get_sheet_name(self):
           return self.section["sheet_name"]
       #获取存储参数的路径
       def get_parameter_path(self):
           return os.path.join(BASE_DIR,self.section["parameter_json"])
       #获取存储预期结果的路径
       def  get_expect_path(self):
           return os.path.join(BASE_DIR, self.section["expect_json"])



if __name__ == '__main__':
    read=Read_Ini()
    print(read.get_excel_path())
