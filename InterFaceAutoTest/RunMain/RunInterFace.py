# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# ProjectName:     Test0805
# FileName:       RunInterFace 
# Author:        MuTou
# Date:         2019/10/16
# Description:
#-------------------------------------------------------------------------------
import  requests
#思考：测试接口
from InterFaceAutoTest.DataOperation.Read_Excel import ReadExcel
from InterFaceAutoTest.ResultOperation.ExpectActualCmp import Expect_Actual_Cmp
from InterFaceAutoTest.RequestOperation.RequestMethod import Request_Method
from InterFaceAutoTest.CommonOperation.PathConstant import Path_Constant
from InterFaceAutoTest.DataOperation.Write_Excel import WriteExcel
from InterFaceAutoTest.DataOperation.ExcelColumn import Excel_Column
from InterFaceAutoTest.DependOperation.DependMethod import Depend_Method
from InterFaceAutoTest.DependOperation.BusinessDependMethod import Business_Depend_Method
from ApiTest.Crm_Connect_Data import Get_Conn
from InterFaceAutoTest.ResultOperation.ExpectActualDataBaseCmp import get_expect_actual_database
class  Run_Main:
       def __init__(self):
           #今天作业：将该部分配置信息写入到ini文件中,要完成相对路径
           #self.rd1 = ReadExcel(Path_Constant.EXCEL_PATH,Path_Constant.SHEET_NAME,Path_Constant.PARAMETER_PATH,Path_Constant.EXPECT_PATH)
           self.rd=WriteExcel(Path_Constant.EXCEL_PATH,Path_Constant.SHEET_NAME,Path_Constant.PARAMETER_PATH,Path_Constant.EXPECT_PATH)
           self.request=Request_Method()
           self.depend=Business_Depend_Method(self.rd,self.request)
           # 创建数据库对象
           self.connect = Get_Conn()
           self.connect1=Get_Conn()

       #实现执行excel中每条测试用例
       def  execute_testcase(self):
           self.cookies=None
           for row in range(2,self.rd.get_max_row()+1):
               get_depend_id=self.rd.get_cell_depend_value(row)
               get_execute = self.rd.get_cell_execute_value(row)
               get_url = self.rd.get_cell_url_value(row)
               get_method = self.rd.get_cell_method_value(row)
               self.get_data = self.rd.get_cell_param_value(row)
               if get_depend_id=="Y" :
                   #if self.depend.get_depend_column_business(row) is None:
                       self.result = self.depend.get_depend_cookie_business(row)
                       self.cookies=self.result[0]
                       if self.result[1]!=None:
                            get_new_data = self.depend.get_response_column_value(self.result, row)
                            self.get_data.update(get_new_data)
                            print("结果是:%s"%get_new_data)
                  # elif self.depend.get_depend_column_cookie(row) is None:
                      # print("业务依赖的结果：%s"%self.depend.get_depend_cookie_business(row))
                  # else:
                      # print("同时依赖%s"%self.depend.get_depend_cookie_business(row))

                  # print("依赖的行：%s" % self.depend.get_depend_row(row))
                   #print("依赖的cookie:%s"%self.depend.get_depend_cookie(row))
               #在此处判断是否需要携带cookie参数
               if get_url != None and get_method!=None:
                   if get_execute=="Y":
                       if self.rd.get_cell_value(Excel_Column.CASE_PARAM, row) == self.rd.get_cell_value(
                               Excel_Column.CASE_EXPECT, row):
                           get_before_count=self.connect.get_table_count("jinke_kehulist")
                           #print(self.get_data)
                           get_actual=self.request.get_respone_actual(get_method,get_url,self.get_data,cookies=self.cookies)
                           get_after_count=self.connect1.get_table_count("jinke_kehulist")
                           print("插入前：",get_before_count)
                           print("插入后：",get_after_count)
                       #获取请求的键值与预期的键值进行比较
                           if get_before_count!=get_after_count:
                               print(self.get_data)
                               get_cmp=get_expect_actual_database(self.get_data,ccompany="lisi")
                               get_result=self.connect.get_select_table("jinke_kehulist","and",ccompany="lisi",cid=get_after_count[0][0])
                       #print(get_actual)
                       #print(self.rd.get_expect_result(row))
                       #print("flag的值是：%s"%self.request.FlagType)
                               self.rd.write_actual_result_value(row,get_cmp)
                       else:
                           get_actual = self.request.get_respone_actual(get_method, get_url, self.get_data,
                                                                        cookies=self.cookies)
                           get_cmp = self.rd.get_expect_actual_cpm(get_actual, row, self.request.FlagType)
                           self.rd.write_actual_result_value(row, get_cmp)
                       #读写流冲突、获取对象返回值赋值问题
                       #self.rd.get_write_object.save(Path_Constant.EXCEL_PATH)
                       #将结果直接写入到excel中，所以现在需要封装excel的写入结果的代码
                       #print("运行的结果是%s"%get_cmp)
if __name__ == '__main__':
    run=Run_Main()
    run.execute_testcase()











