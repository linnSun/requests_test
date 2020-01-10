# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# ProjectName:     Test0805
# FileName:       ExpectActualDatabaseCmp 
# Author:        MuTou
# Date:         2019/10/21
# Description:
#-------------------------------------------------------------------------------
from ApiTest.Crm_Connect_Data import Get_Conn
#class Expect_Actual_DataBase_Cmp(Expect_Actual_Cmp):
    #实现预期与实际的比较：实际结果是根据传入的表、条件返回的列表的元组对象
def  get_expect_actual_database(data,**kwargs):
        # connect=Get_Conn()
        # get_actual=connect.get_select_table(tableName,args,kwargs)
        # get_count=connect.get_table_count(tableName)
        expect_dict={}
        actual_dict={}
        for key,value in kwargs.items():
            if value not in data:
                actual_dict[key]=value
        return "expect:%s\nactual:%s"%(expect_dict,actual_dict)
























