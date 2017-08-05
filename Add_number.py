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


class Add_number(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def test_test2(self):
        wd = self.wd
        self.Open_home_page(wd)

        self.Login(wd, "tolikivanyuk@gmail.com", "ihor198q")

        wd.find_element_by_link_text("History").click()
        wd.find_element_by_link_text("New SMS").click()
        wd.find_element_by_id("newMsgRecipient").click()
        wd.find_element_by_id("newMsgRecipient").send_keys("+380971779383")
        wd.find_element_by_id("newMsgText").click()
        wd.find_element_by_id("newMsgText").send_keys("Hello!!!")
        wd.find_element_by_id("sendNowBtn").click()
        wd.find_element_by_link_text("Tolik Ivanyuk").click()
        wd.find_element_by_name("Notifications").click()


    def Login(self, wd, username, password):
        wd.find_element_by_id("_username").click()
        wd.find_element_by_id("_username").send_keys(username)
        wd.find_element_by_id("_password").click()
        wd.find_element_by_id("_password").send_keys(password)
        wd.find_element_by_id("logInBtn").click()

    def Open_home_page(self, wd):
        wd.get("https://my.textmagic.com/login")

    def tearDown(self):
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()
