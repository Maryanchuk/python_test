# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class 111(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_111(self):
        success = True
        wd = self.wd
        wd.get("https://my.textmagic.com/login")
        ActionChains(wd).move_to_element(wd.find_element_by_css_selector("div.app-markets")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_css_selector("div.col-md-6.login-ad")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_css_selector("div.panel-body.reopen-account")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_css_selector("div.form-group.has-pass-toggle ")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_id("logInFrm")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_id("_username")).perform()
        wd.find_element_by_id("_username").click()
        ActionChains(wd).move_to_element(wd.find_element_by_css_selector("div.form-group.has-pass-toggle ")).perform()
        wd.find_element_by_id("_password").click()
        wd.find_element_by_id("_password").send_keys("\\undefined")
        ActionChains(wd).move_to_element(wd.find_element_by_id("_password")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_id("logInFrm")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_id("logInBtn")).perform()
        wd.find_element_by_id("_username").click()
        wd.find_element_by_id("_username").send_keys("\\undefined")
        wd.find_element_by_id("logInBtn").click()
        ActionChains(wd).move_to_element(wd.find_element_by_css_selector("div.mask-text")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_id("chat-contact-list-scroll-content")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_xpath("//div[@id='chat-contact-list-content']/div[6]")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_xpath("//div[@id='chat-contact-list-content']/div[5]")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_xpath("//div[@id='chat-contact-list-content']/div[2]/div[2]")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_xpath("//div[@id='chat-contact-list-content']//div[.='Q Q']")).perform()
        wd.find_element_by_id("//div[@id='chat-contact-list-content']//div[.='Q Q']").click()
        ActionChains(wd).move_to_element(wd.find_element_by_xpath("//div[@id='chat-contact-list-content']//div[.='qqq']")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_xpath("//div[@id='chat-contact-list-content']//div[.='Oleg Kit']")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_xpath("//div[@id='i15707067']/label/div/div[2]")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_id("newMsgText")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_id("textmagic-ws-chat")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_css_selector("body")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_css_selector("body")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_id("textmagic-ws-chat")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_css_selector("body")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_id("thread-tabs-l1-close")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_xpath("//div[@class='chat-contact-tabs']//li[.='Closed']")).perform()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
