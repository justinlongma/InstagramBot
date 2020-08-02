# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from selenium import webdriver
from time import sleep

'''Bot that Navigates to instagram site and withdraws followers/following information'''
class InstaBot:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome(executable_path='/InstagramBot/chromedriver')
        #navigate to instagram website
        self.driver.get('https://instagram.com')
        sleep(2)
        #input login information
        userfield = self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
        passfield = self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(password)
        sleep(2)
        #click login button
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div").click()
        sleep(3)
        #check to see if there is a "not now"button (sometimes appears)
        try:
            self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]").click()
        except:
            print('huh')
        #navigate to profile
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/a/img").click()
        sleep(2)
        follow = self.driver.find_element_by_xpath("//a[contains(@href,'/following')]").click()
        
        
        
        
        
        
        
        
        self.driver.execute_script("arguments[0].scrollIntoView()",follow)
        
        
        
        
        
        
#InstaBot('INSERT USERNAME HERE','INSERT PASSWORD HERE')

