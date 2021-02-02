from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import keyboard
from keyboard._keyboard_event import KeyboardEvent
import random

class WhatBot:

    def __init__(self, contact):
        self.contact = contact
        self.driver = webdriver.Firefox(executable_path=r"C:/Users/Admin/Documents/python/whats/geckodriver.exe")#Seu navegador assim como o caminho para o geckodriver 


    def Contact(self):
            driver = self.driver
            driver.get('https://web.whatsapp.com/')
            time.sleep(20)
            contact_element = driver.find_element_by_xpath("//span[@title='{}']".format(self.contact))
            contact_element.click()

    def SendMsg(self):
        driver = self.driver
        while True:
                time.sleep(1)
                msg = ['Eu sei o que você fez','Eu farei justiça!','Ainda dá tempo pra fugir!','Sou um pescotapa!!HAHAHA']
                msg_element = driver.find_element_by_xpath("//div[@class='_1awRl copyable-text selectable-text' and contains(@data-tab,'6')]")
                msg_element.clear()
                for x in range(len(msg)): 
                        msg_element.send_keys(msg[x])
                        msg_element.send_keys(Keys.ENTER)
        else:
                print('Msg done!')

johnBot = WhatBot('Whats test')
johnBot.Contact()
johnBot.SendMsg()