# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# ProjectName:     Test0805
# FileName:       ExpectActualCmp 
# Author:        MuTou
# Date:         2019/10/17
# Description:
#-------------------------------------------------------------------------------
from InterFaceAutoTest.DataOperation.Read_Excel import ReadExcel
class Expect_Actual_Cmp(ReadExcel):
    #需要完成预期结果与实际结果的比较
    #先获取预期结果：
    def get_expect_result(self,rowNum):
        return self.get_cell_expect_value(rowNum)
    #实现预期与实际比较
    def get_expect_actual_cpm(self,actualValue,rowNum,FlagType):
        #获取当前的标记状态：
        if FlagType==True:
            return self.get_expect_actual_json_cpm(actualValue,rowNum)
        else:
            return self.get_expect_actual_html_cmp(actualValue,rowNum)

    #声明一个方法实现json格式数据与html格式数据比较
    def  get_expect_actual_html_cmp(self,actualValue,rowNum):
        try:
            expectValue = self.get_expect_result(rowNum)
            newExpectValue={}
            for key,value in expectValue.items():
                if value not  in actualValue:
                    newExpectValue[key]=value
            if len(newExpectValue)==0:
                return "预期与实际一致"
            return "expect:%s"%newExpectValue
        except:
            return "没有定义预期结果"
    #两个json数据格式比较
    def get_expect_actual_json_cpm(self,actualValue,rowNum):
        #预期比实际多、实际比预期多、值不一样、两者完全一样
        #可以通过集合中的^ 进行完成，但是只能够获取键多对应值的差异数据
        #思路：获取比较的标准；
        #expectValue={'msg': '用户不存在！', 'code': '1',"text":"helloworld"}
        expectValue = self.get_expect_result(rowNum)
        try:
            #actualValue={'msg': '用户不存在！', 'code': '1',"text":"helloworld"}
            expectActualValue={}
            expectActualValue.update(expectValue)
            expectActualValue.update(actualValue)
            newExpectValue={}
            newActualValue={}
            for  key,value in expectActualValue.items():
                #如果此处的键不在预期字典，那就说明在实际的结果值中
                if  key not in expectValue:
                    newActualValue[key]=actualValue[key]
                elif key not in actualValue:
                    newExpectValue[key]=expectValue[key]
                else:
                    if expectValue[key]!=actualValue[key]:
                        newActualValue[key] = actualValue[key]
                        newExpectValue[key] = expectValue[key]
                    #如果直接在当前if中确定else语句块中的结果为两个结果一致时直接返回，则如果第一个键值
                    #相等直接返回
            if len(newExpectValue)==0 and len(newActualValue)==0:
                return "预期与实际一致"
            return "expect:%s\nactual:%s"%(newExpectValue,newActualValue)
        except:
            return "expect:%s\nactual:%s"%(expectValue,actualValue)


#如果需要定义写入excel的数据格式样式的话可以使用openpyxl模块中存在一个样式库from openpyxl.styles
# if __name__ == '__main__':
#     result=Expect_Actual_Cmp()
#     print(result.get_expect_actual_cpm(1,3))

        #需要考虑分析实际结果与预期结果的类型：
        #json格式的数据与html格式的数据比较
        #json格式的数据与dict格式的数据比较
        # 预期是以下内容：如果是json与dict格式的数据比较实现以下内容的显示
        # {'msg': '用户不存在！', 'code': '1',"text":"helloworld'}
        # 实际内容：
        # {'msg': '用户不存在！', 'code': '0'}
        # expect:{'code': '1',"text":"helloworld'}
        # actual:{'code': '0'}
        #如果是json格式数据与html页面数据：只需要将预期结果的值在html页面中无法找到内容的键值对进行显示





















