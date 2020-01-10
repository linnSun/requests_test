# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# ProjectName:     Test0805
# FileName:       conftest 
# Author:        MuTou
# Date:         2019/10/25
# Description:固件夹具的初始化对象全部定义在当前文件中
#-------------------------------------------------------------------------------
from InterFaceAutoTest.RequestOperation.RequestMethod import Request_Method
from InterFaceAutoTest.CommonOperation.PathConstant import Path_Constant
from InterFaceAutoTest.DataOperation.Write_Excel import WriteExcel
from InterFaceAutoTest.DependOperation.BusinessDependMethod import Business_Depend_Method
from ApiTest.Crm_Connect_Data import Get_Conn
import pytest
#先定义一个请求对象的初始化：作用域：function
@pytest.fixture(scope="function")
def get_request():
    return Request_Method()

#定义读取excel的对象初始化：作用域：module、session
@pytest.fixture(scope="session")
def get_rd():
    return WriteExcel(Path_Constant.EXCEL_PATH, Path_Constant.SHEET_NAME, Path_Constant.PARAMETER_PATH,
                     Path_Constant.EXPECT_PATH)

#定义的依赖对象的初始化：作用域：function
@pytest.fixture(scope="function")
def get_depend(get_request,get_rd):
    #固件对象之间fixture的相互调用
    return Business_Depend_Method(get_rd,get_request)

#定义创建数据库对象的初始化：作用域：module、session
@pytest.fixture(scope="session")
def get_connect():
    return Get_Conn()


from datetime import datetime
from py._xmlgen import html
import time
#实现结果表格的头定义
# You can modify the columns by implementing custom hooks for the header and rows.
# The following example conftest.py adds a description column with the
# test function docstring, adds a sortable time column, and removes the links column:
#增加了一个描述列（用于进行获取函数的doc文档注释），还增加了一个已排序好的时间列，最后移除了links列
#下面代码的实现就是上面英文那句话的描述
def pytest_html_results_table_header(cells):
    cells.insert(2, html.th('Description'))
    cells.insert(1, html.th('Time', class_='sortable time', col='time'))
    # cells.pop()
#声明表头之后，需要获取对应头的每行的数据
def pytest_html_results_table_row(report, cells):
    cells.insert(2, html.td(report.description))
    cells.insert(1, html.td(time.strftime("%Y-%m-%d %H-%M-%S",time.localtime()), class_='col-time'))
    # cells.pop()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    #此句代码就是实现模块中函数的doc注释的内容，将其内容结果写入到报告指定的列中
    report.description = str(item.function.__doc__)


# #实现报告中的附件添加（截图---->失败截图）
# # import pytest
# # @pytest.hookimpl(hookwrapper=True)
# # def pytest_runtest_makereport(item, call):
# #     pytest_html = item.config.pluginmanager.getplugin('html')
# #     outcome = yield
# #     report = outcome.get_result()
# #     extra = getattr(report, 'extra', [])
# #     if report.when == 'call' or report.when=="setup":
# #         #extra.append(pytest_html.extras.url('http://www.example.com/'))
# #         xfail = hasattr(report, 'wasxfail')
# #         #可以声明附件：如果web自动化的话则可以直接使用驱动器对象直接调用get_screenshot_as_png
# #         get_file_name=""
# #         if (report.skipped and xfail) or (report.failed and not xfail):
# #             # only add additional html on failure
# #             extra.append(pytest_html.extras.html("<img src=''>"))
# #         report.extra = extra



# class  A:
#     def __call__(self):
#         print("调用call方法")
#
# a=A()
# #将a（实例化的）对象当做一个函数对象处理
# a.__call__()
# #a()


















