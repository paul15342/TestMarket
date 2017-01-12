# coding=utf-8
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

def LoginInput(self,username,passwd):
    driver=self.driver
    driver.find_element_by_id('username').send_keys(username)
    driver.find_element_by_id('password').send_keys(passwd)
    time.sleep(1)
    driver.find_element_by_xpath("//form[@id='loginForm']/input[@type='submit']").click()  #登录


def clickActivityList(self):
    driver=self.driver
    #点击活动管理
    driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div[1]/div/div[2]/div[1]/a').click()
    time.sleep(1)
    #点击活动列表
    driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div[1]/div/div[2]/div[2]/div/ul/li[1]/a').click()
    time.sleep(1)

def buildNewActivity(self):
    driver=self.driver
    #点击新建活动
    driver.find_element_by_xpath('//*[@id="searchForm"]/ul/li[3]/a/input').click()

def ChangeFrame(self):
    driver=self.driver
    driver.switch_to_frame('mainFrame') #切换frame

def quiteFrame(self):
    driver=self.driver
    driver.switch_to.parent_frame()

def exit(self):
    driver=self.driver
    driver.find_element_by_xpath('//*[@id="userControl"]/li[2]/a').click()

