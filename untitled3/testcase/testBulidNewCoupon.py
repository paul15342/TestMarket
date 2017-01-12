# -*- coding: utf-8 -*-


import unittest

from selenium import webdriver
from untitled3.Data import data
from untitled3.Login import BulidActivity,login
from untitled3.coupon import newCoupon
import time
import  HTMLTestRunner

class testbuildNewC(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.get('http://10.10.1.168:2019/marketing/a')

    def test_bulid01(self):      #新建
        username= data.ExcelData(1,0)      #用户账号
        passwd= data.ExcelData(1,1)       #用户密码
        login.LoginInput(self,username,passwd)
        newCoupon.newCoupon(self)
        login.ChangeFrame(self)
        newCoupon.buildCoupon(self)
        newCoupon.saveCoupon(self)

        msg=self.driver.find_element_by_xpath('/html/body/ul[1]/li[1]/a')
        print msg.text
        self.assertEqual('Admin Portal',self.driver.title)
        self.assertEqual(u'投资业务',msg.text)

    def tearDown(self):
        self.driver.quit()

if __name__=='__main__':
    testsuit= unittest.TestSuite()
    testsuit.addTest(testbuildNewC('test_bulid01'))  #将测试用例加入到测试容器中
    fp=file("E:\\report\\testresult3.html","wb")     #wb 写 覆盖   #f=file("d:/111.html","wb")
    print 'pass'
    #设置测试报告的标题等
    runner=HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'测试报告',
        description=u'用例执行情况：')
    print 'pass2'
    runner.run(testsuit)
        #执行测试用例
    fp.close()
