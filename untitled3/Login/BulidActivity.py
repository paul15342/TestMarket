
# -*- coding: utf-8 -*

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

def bulidNewActivity(self,name,way,action,attribute):
    driver=self.driver
    #输入活动名称

    driver.find_element_by_xpath('/html/body/form[1]/table/tbody/tr[1]/td[2]/div/div/input').send_keys(name)
    #选择下发方式
    Select(driver.find_element_by_id('distributeWayNum')).select_by_value(way)
    time.sleep(2)
    driver.find_element_by_xpath(action).click() #选择下发对象用户动作为注册
    time.sleep(1)
    driver.find_element_by_xpath(attribute).click()  #选择用户属性、

def chooseTime(self):
    driver=self.driver
    #时间插件开始时间
    js = "$('input[id=activityStartTime]').removeAttr('readonly')"
    driver.execute_script(js)
    time.sleep(1)
    driver.find_element_by_id('activityStartTime').send_keys('2016-01-05 15:05')
    time.sleep(1)
    print driver.find_element_by_id('activityStartTime').get_attribute('value')

    #时间插件输入结束时间
    js = "$('input[id=activityEndTime]').removeAttr('readonly')"
    driver.execute_script(js)
    time.sleep(1)
    driver.find_element_by_id('activityEndTime').send_keys('2017-01-30 15:05')
    time.sleep(1)

def setCoupon(self):
    driver=self.driver
    driver.find_element_by_id('btnSubmit').click()#点击配置卡卷
    time.sleep(1)

def chooseCouponType(self,couponType):
    driver=self.driver
    #选择卡卷类型
    driver.find_element_by_id(couponType).click() #选择5元体验金
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="inputForm"]/div[3]/div/label[2]/input').click()
    driver.find_element_by_xpath("//*[@id='couponValidityDay']").send_keys(5)

def saveCoupon(self):
    driver=self.driver
    driver.find_element_by_id("btnSubmit").click()  #点击保存卡卷
    time.sleep(2)
    driver.find_element_by_xpath("//input[@id='btnPulish']").click() #点击发布
    time.sleep(4)
    driver.save_screenshot('2.jpg') #保存图片


