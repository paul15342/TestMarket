#coding=utf-8

from selenium import webdriver
import random

def newCoupon(self):
    driver=self.driver
    #点击卡卷管理
    driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[1]/div/div[1]/div[2]/div/ul/li[3]/a").click()
    #点击卡卷类别
    driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div[1]/div/div[1]/div[2]/div/ul/li[3]/ul/li[2]/a').click()
    print driver.title

def buildCoupon(self):
    driver=self.driver
    driver.find_element_by_id('addBtn').click()  #点击新增
    #随机输入卡卷的大小
    Number=random.randint(99,199)
    driver.find_element_by_id('couponContent').send_keys(Number)

def saveCoupon(self):
    driver=self.driver
    #点击保存
    driver.find_element_by_xpath('//div[@class=\'form-actions\']/input[@id=\'addBtn\']').click()

