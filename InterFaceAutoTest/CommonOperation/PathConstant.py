# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# ProjectName:     Test0805
# FileName:       PathConstant 
# Author:        MuTou
# Date:         2019/10/17
# Description:
#-------------------------------------------------------------------------------
from InterFaceAutoTest.CommonOperation.ReadIni import Read_Ini
def  get_read_ini():
    return Read_Ini()
class Path_Constant:
    EXCEL_PATH=get_read_ini().get_excel_path()
    PARAMETER_PATH=get_read_ini().get_parameter_path()
    EXPECT_PATH=get_read_ini().get_expect_path()
    SHEET_NAME=get_read_ini().get_sheet_name()








