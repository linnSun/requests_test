# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# ProjectName:     Test0805
# FileName:       Write_Excel 
# Author:        MuTou
# Date:         2019/10/17
# Description:
#-------------------------------------------------------------------------------
from InterFaceAutoTest.ResultOperation.ExpectActualCmp import Expect_Actual_Cmp
from InterFaceAutoTest.CommonOperation.PathConstant import Path_Constant
from InterFaceAutoTest.DataOperation.ExcelColumn import Excel_Column
from openpyxl import load_workbook
class WriteExcel(Expect_Actual_Cmp):
        #实现赋值操作；
        #实现实际结果的值写入操作
        def  write_actual_value(self,rowNum,actualValue):
            self.get_Write_Sheet[Excel_Column.CASE_ACTUAL + str(rowNum)]=str(actualValue)
            # self.write_actual=self.get_cell_actual_object(rowNum)
            # self.write_actual=actualValue
        #实现是否通过值的写入操作
        def  write_result_value(self,rowNum,actualValue):
            if actualValue=="预期与实际一致":
                self.get_Write_Sheet[Excel_Column.CASE_RESULT + str(rowNum)]="通过"
            else:
                self.get_Write_Sheet[Excel_Column.CASE_RESULT + str(rowNum)]="不通过"
        #将以上两个方法封装到一个方法中，并实现保存操作
        def  write_actual_result_value(self,rowNum,actualValue):
            self.write_actual_value(rowNum,actualValue)
            self.write_result_value(rowNum,actualValue)
            self.get_write_object.save(Path_Constant.EXCEL_PATH)

























