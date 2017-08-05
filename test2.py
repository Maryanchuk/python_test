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

class test2(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_test2(self):
        success = True
        wd = self.wd
        wd.get("http://bugs8.gatserver.com/login")
        ActionChains(wd).move_to_element(wd.find_element_by_id("login_menu_panes")).perform()
        wd.find_element_by_id("login_menu_panes").click()
        ActionChains(wd).move_to_element(wd.find_element_by_css_selector("div.logindiv.regular")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_id("tbg3_username")).perform()
        wd.find_element_by_id("tbg3_username").click()
        wd.find_element_by_id("tbg3_password").click()
        wd.find_element_by_id("tbg3_password").send_keys("tolikivanyuk")
        ActionChains(wd).move_to_element(wd.find_element_by_id("maintd")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_css_selector("div.logindiv.regular")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_xpath("//form[@id='login_form']/div[2]")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_id("login_button")).perform()
        wd.find_element_by_id("tbg3_username").click()
        wd.find_element_by_id("tbg3_username").send_keys("Anatoliii")
        wd.find_element_by_id("login_button").click()
        ActionChains(wd).move_to_element(wd.find_element_by_xpath("//form[@id='login_form']/div[2]")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_id("maintd")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_css_selector("td.main_area")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_xpath("//div[@id='dashboard_11034']/table/tbody/tr[6]/td[2]")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_link_text("Bug report YVW004-71 - [Windows 7] [Internet Explorer] Expand button does not work")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_xpath("//li[@id='dashboard_container_11035']/div")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_id("searchfor")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_xpath("//nav[@id='header_userinfo']/ul/li")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_link_text("anatoliiI")).perform()
        wd.find_element_by_link_text("anatoliiI").click()
        ActionChains(wd).move_to_element(wd.find_element_by_css_selector("div.header")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_link_text("Logout")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_link_text("Issues reported by me")).perform()
        wd.find_element_by_link_text("Issues reported by me").click()

        wd.find_element_by_xpath("//div[@id='search_results']//button[.='Last page ⇥']").click()
        ActionChains(wd).move_to_element(wd.find_element_by_xpath("//div[@id='search_results']//button[.='36']")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_xpath("//div[@id='search_results']//button[.='24']")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_xpath("//div[@id='search_results']//button[.='6']")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_xpath("//div[@id='search_results']/div[4]/div")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_id("search_bulk_container_bottom")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_id("search_results")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_xpath("//div[@id='search_results']//button[.='20']")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_xpath("//td[@class='footer_bar']/footer/table/tbody/tr/td")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_css_selector("td.footer_bar")).perform()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
