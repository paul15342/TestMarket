
# -*- coding: -utf-8 -*-

from selenium import webdriver
import time,random
from selenium.webdriver.support.ui import Select


driver=webdriver.Firefox()
driver.implicitly_wait(10)
driver.get('http://10.10.1.168:2019/marketing/a ')
time.sleep(2)
driver.set_window_size(600,600)
driver.maximize_window()
driver.get_window_size()

print '-'*50
#getTime
getTime='%Y-%m-%d %X'
print time.strftime(getTime,time.localtime())

driver.find_element_by_id('username').send_keys('xionghl')
driver.find_element_by_id('password').send_keys('Hl123456')
time.sleep(1)
driver.find_element_by_xpath("//form[@id='loginForm']/input[@type='submit']").click() #点击登录
time.sleep(3)

#点击卡卷管理
driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[1]/div/div[1]/div[2]/div/ul/li[3]/a").click()
#点击卡卷类别
driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div[1]/div/div[1]/div[2]/div/ul/li[3]/ul/li[2]/a').click()
driver.switch_to_frame('mainFrame')
print driver.title
time.sleep(2)
driver.find_element_by_id('addBtn').click()  #点击新增
list= ("10010003","10010004","10010002","10010001")
a=random.randint(0,3)
i=list[a]
Select(driver.find_element_by_name('couponTypeSel')).select_by_value(i)
#driver.find_element_by_xpath('/html/body/div[1]/form/div[2]/div/select/option[1]')

#随机输入卡卷的大小
Number=random.randint(0,99)
driver.find_element_by_id('couponContent').send_keys(Number)
driver.find_element_by_xpath('//div[@class=\'form-actions\']/input[@id=\'addBtn\']').click()#点击保存

driver.quit()