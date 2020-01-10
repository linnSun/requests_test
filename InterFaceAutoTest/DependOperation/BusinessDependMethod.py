# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# ProjectName:     Test0805
# FileName:       BusinessDependMethod 
# Author:        MuTou
# Date:         2019/10/18
# Description:
#-------------------------------------------------------------------------------
from InterFaceAutoTest.DependOperation.DependMethod import Depend_Method
class Business_Depend_Method(Depend_Method):
          #取出指定字段所对应响应体的值;先默认响应的结果数据格式是json
          def get_response_column_value(self,resultObject,rowNum):
              dict1={}
              get_columns=self.get_from_depend_value(rowNum)
              if get_columns[0] in resultObject[1]:
                  if get_columns[1]!=None:
                     dict1[get_columns[1]]=resultObject[1][get_columns[0]]
                     return dict1
                  else:
                      dict1[get_columns[0]]=resultObject[1][get_columns[0]]
                      return dict1
              return dict1























