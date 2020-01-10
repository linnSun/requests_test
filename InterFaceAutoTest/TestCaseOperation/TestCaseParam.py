# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# ProjectName:     Test0805
# FileName:       TestCaseParam 
# Author:        MuTou
# Date:         2019/10/25
# Description:该模块的功能实现与RunMain中RunInterFace的功能实现等价的
#-------------------------------------------------------------------------------
from InterFaceAutoTest.DataOperation.ExcelColumn import Excel_Column
from InterFaceAutoTest.CommonOperation.PathConstant import Path_Constant
from InterFaceAutoTest.DataOperation.Write_Excel import WriteExcel
from InterFaceAutoTest.DataOperation.ExcelColumn import Excel_Column
from InterFaceAutoTest.ResultOperation.ExpectActualDataBaseCmp import get_expect_actual_database
#需要完成参数化，第一件事情：分析获取到什么格式的数据需要提前定义好，将之前的main方法中的代码先进行封装
#第二件事情：所需要参数化的数据格式已经定义好，进行获取获取数据
#get_depend_id, get_execute, get_method, get_url, get_data, row
#声明一个函数用于进行获取上述格式的数据
import allure
def  get_format_value():
    rd = WriteExcel(Path_Constant.EXCEL_PATH, Path_Constant.SHEET_NAME, Path_Constant.PARAMETER_PATH,
                         Path_Constant.EXPECT_PATH)
    #list_value=[]
    for row in range(2, rd.get_max_row() + 1):
        get_depend_id = rd.get_cell_depend_value(row)
        get_execute = rd.get_cell_execute_value(row)
        get_url = rd.get_cell_url_value(row)
        get_method = rd.get_cell_method_value(row)
        get_data = rd.get_cell_param_value(row)
        get_expect=rd.get_cell_expect_value(row)
        #list_value.append([get_depend_id,get_execute,get_method,get_url,get_data,row])
        if get_execute=="Y":
            yield [get_depend_id,get_execute,get_method,get_url,get_data,row,get_expect]
    #return list_value

import pytest
class TestCaseParam:
    def check_depend_id(self,get_depend_id,get_data,get_depend,row):
        if get_depend_id == "Y":
            self.result = get_depend.get_depend_cookie_business(row)
            self.cookies = self.result[0]
            if self.result[1] != None:
                get_new_data = get_depend.get_response_column_value(self.result, row)
                get_data.update(get_new_data)
    #判断是否执行
    def check_execute(self,get_execute,get_method,get_url,get_data,get_rd,get_connect,get_request,row):
        if get_url != None and get_method != None:
            #if get_execute == "Y":
                if get_rd.get_cell_value(Excel_Column.CASE_PARAM, row) == get_rd.get_cell_value(
                        Excel_Column.CASE_EXPECT, row):
                    get_before_count = get_connect.get_table_count("jinke_kehulist")
                    self.get_actual = get_request.get_respone_actual(get_method, get_url, get_data,
                                                                 cookies=self.cookies)
                    #self.get_expect=get_rd.get_cell_expect_value(row)
                    get_after_count =get_connect.get_table_count("jinke_kehulist")
                    print("插入前：", get_before_count)
                    print("插入后：", get_after_count)
                    # 获取请求的键值与预期的键值进行比较
                    if get_before_count != get_after_count:
                        print(get_data)
                        get_cmp = get_expect_actual_database(get_data, ccompany="lisi")
                        get_result = get_connect.get_select_table("jinke_kehulist", "and", ccompany="lisi",
                                                                   cid=get_after_count[0][0])
                        get_rd.write_actual_result_value(row, get_cmp)
                else:
                    self.get_actual = get_request.get_respone_actual(get_method, get_url, get_data,
                                                                 cookies=self.cookies)
                    get_cmp = get_rd.get_expect_actual_cpm(self.get_actual, row, get_request.FlagType)
                    get_rd.write_actual_result_value(row, get_cmp)

    def check_all(self,get_rd,get_connect,get_depend,get_request,get_depend_id,get_execute,get_method,get_url,get_data,row):
        #self.get_actual=None
        self.check_execute(get_execute,get_method,get_url,get_data,get_rd,get_connect,get_request,row)
        self.check_depend_id(get_depend_id, get_data, get_depend, row)

    #get_depend_id, get_execute, get_method, get_url, get_data, row
    @pytest.mark.repeat(3)
    @allure.step("这是实现测试框架的参数化操作")
    @allure.description("接口参数化")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("get_value",[value for value in get_format_value()])
    def test_all(self,get_rd,get_connect,get_depend,get_request,get_value):
        """
        :param get_rd:
        :param get_connect:
        :param get_depend:
        :param get_request:
        :param get_value:
        :return:
        """
        get_expect=get_value[-1]
        self.cookies = None
        self.check_all(get_rd,get_connect,get_depend,get_request,*get_value[:-1])
        # print(get_expect)
        # print("实际结果是：",self.get_actual)
        assert self.get_actual==get_expect

if __name__ == '__main__':
    pytest.main()























