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


class text_megic(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def test_text_megic(self):

        wd = self.wd
        wd.get("https://my.textmagic.com/login")



        wd.find_element_by_id("_username").click()
        wd.find_element_by_id("_username").clear()
        wd.find_element_by_id("_username").send_keys("tolikivanyuk@gmail.com")

        wd.find_element_by_id("_password").click()
        wd.find_element_by_id("_password").clear()
        wd.find_element_by_id("_password").send_keys("ihor198q")

        wd.find_element_by_id("logInBtn").click()

        wd.find_element_by_link_text("Account").click()

        wd.find_element_by_id("").click()






    def tearDown(self):
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()
