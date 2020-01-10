# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# ProjectName:     Test0805
# FileName:       DependMethod 
# Author:        MuTou
# Date:         2019/10/18
# Description:
#-------------------------------------------------------------------------------
class  Depend_Method:
    def __init__(self,readObject,requestObject):
        self.readObject=readObject
        self.requestObject=requestObject
    #获取是否依赖的列数据值:如果需要调用read_excel模块中的方法则：创建对象、继承Read_Excel
    #对象创建但是太多了；如果是继承，则在主程序入口创建该模块对象的时候，又需要传入Read_Excel当中的
    #所有的参数 :获取依赖cookie那一列是否存在值
    def  get_depend_column_cookie(self,rowNum):
        #get_depend_value=self.readObject.get_cell_depend_value(rowNum)
        #get_business_value=readObject.get_cell_business_value(rowNum)
        get_cookie_value=self.readObject.get_cell_cookie_value(rowNum)
        #if get_depend_value=="Y":
        if get_cookie_value is not None:
            return get_cookie_value

    #已经取到需要关联接口的用例ID，需要获取到对应用例的行，将业务数据、cookie数据都封装在该方法中
    def get_depend_row(self,columnValue):
        get_max_row=self.readObject.get_max_row()
        for row in range(2,get_max_row+1):
            get_case_id=self.readObject.get_cell_id_value(row)
           # if get_case_id==self.get_depend_column_cookie(rowNum):
            if get_case_id == columnValue:
                return row


    def get_object(self,get_depend_row):
        get_depend_url = self.readObject.get_cell_url_value(get_depend_row)
        get_depend_method = self.readObject.get_cell_method_value(get_depend_row)
        get_depend_data = self.readObject.get_cell_param_value(get_depend_row)
        return (get_depend_method,get_depend_url,get_depend_data)

    #通过行进行执行所依赖的那条用例并返回该接口响应结果的cookies
    def get_depend_cookie_business(self,rowNum):
        get_depend_row_cookie=self.get_depend_row(self.get_depend_column_cookie(rowNum))
        get_depend_row_business = self.get_depend_row(self.get_depend_column_business(rowNum))
        if get_depend_row_cookie!=None and get_depend_row_business!=None:
            get_resp=self.requestObject.get_respone_actual(*self.get_object(get_depend_row_business))
            get_cookie=self.requestObject.get_respone_cookie(*self.get_object(get_depend_row_cookie))
            return [get_cookie,get_resp]
        elif get_depend_row_cookie!=None and get_depend_row_business==None:
            return [self.requestObject.get_respone_cookie(*self.get_object(get_depend_row_cookie)),None]
        elif get_depend_row_cookie==None and get_depend_row_business!=None:
            return [None,self.requestObject.get_respone_actual(*self.get_object(get_depend_row_business))]


    #获取依赖业务数据的字段
    def  get_depend_column_business(self,rowNum):
        get_business_value = self.readObject.get_cell_business_value(rowNum)
        if get_business_value is not None:
            return get_business_value


    #根据依赖的行进行取出被依赖的字段、依赖的字段
    def  get_from_depend_value(self,rowNum):
        get_row=self.get_depend_row(self.get_depend_column_business(rowNum))
        if get_row!=None:
            return [self.readObject.get_cell_from_depend_column_value(get_row),self.readObject.get_cell_depend_column_value(get_row)]



    #分析：
    #还需要判断是否依赖其他接口业务上的数据；（上下游接口）
    #分析：业务数据的响应数据格式（json、其他格式）；需要获取依赖接口的数据字段；最后将获取的字段
    #传递到指定的请求头中；
    #A   ：{username:"lisi"}
    #B  ：第一种情况：B中压根就没有该字段，则直接将该字段添加即可；第二种情况：有字段
    #但是其键不同需要获取其值；键相同；{"name"：？}



























