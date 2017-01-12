# -*- coding: utf-8 -*-


import unittest
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from selenium import webdriver
from untitled3.Data import data
from untitled3.Login import BulidActivity,login
from untitled3.coupon import newCoupon
import time
import HTMLTestRunner

from selenium.webdriver.support.ui import Select

class testbuildNewA(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.get('http://10.10.1.168:2019/marketing/a')

    def test_bulid01(self):      #新建活动
        username= data.ExcelData(1,0)      #用户账号
        passwd= data.ExcelData(1,1)       #用户密码
        name=data.ExcelData(1,2)          #活动名称
        way=data.ExcelData(1,3)          #下发方式
        action=data.ExcelData(1,5)       #用户动作
        attribute=data.ExcelData(1,7)    #下发属性
        couponType=data.ExcelData(1,9)   #卡卷类型
        print username,passwd
        login.LoginInput(self,username,passwd)  #登录
        login.clickActivityList(self)  #点击活动列表
        login.ChangeFrame(self)       #切换frame
        login.buildNewActivity(self)
        BulidActivity.bulidNewActivity(self,name,way,action,attribute) #输入第一页面信息
        BulidActivity.chooseTime(self)
        BulidActivity.setCoupon(self)   #点击建立卡卷
        BulidActivity.chooseCouponType(self,couponType)
        BulidActivity.saveCoupon(self)
        login.quiteFrame(self)
        login.exit(self)               #退出当前账号

    def tearDown(self):
        print ('Test Pass')

if __name__=='__main__':

    testunit = unittest.TestSuite()
    testunit.addTest(testbuildNewA('test_bulid01'))  #将测试用例加入到测试容器中
    filename = r'E:\report\testresult1.html'
    f=file(filename ,"wb")     #wb 写 覆盖   #f=file("d:/111.html","wb")
    assert f,'Fault'
    #设置测试报告的标题等
    runner=HTMLTestRunner.HTMLTestRunner(stream=f,title=u'测试报告',description=u'用例执行情况：')

    runner.run(testunit)    #执行测试用例
    f.close()