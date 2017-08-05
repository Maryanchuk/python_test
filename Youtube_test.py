# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class Youtube_test(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_Youtube_test(self):
        success = True
        wd = self.wd
        wd.get("https://www.youtube.com/")
        ActionChains(wd).move_to_element(wd.find_element_by_id("appbar-nav")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_id("yt-masthead-container")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_id("masthead-search-terms")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_id("masthead-search-term")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_id("masthead-search-term")).perform()
        wd.find_element_by_id("masthead-search-term").click()
        wd.find_element_by_id("masthead-search-term").clear()
        wd.find_element_by_id("masthead-search-term").send_keys("best")
        ActionChains(wd).move_to_element(wd.find_element_by_id("gs_tti50")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_id("masthead-search-terms")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_id("search-btn")).perform()
        wd.find_element_by_id("masthead-search-term").click()
        wd.find_element_by_id("masthead-search-term").send_keys("\\undefined")
        wd.find_element_by_id("search-btn").click()
        ActionChains(wd).move_to_element(wd.find_element_by_css_selector("a.gsst_a")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_id("gs_tti50")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_id("yt-masthead-container")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_css_selector("div.filter-crumb-spacer")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_xpath("//ol[@id='section-list-026204']/li[1]/div")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_xpath("//div[@class='pyv-afc-ads-container']/div[1]/div")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_link_text("7 условий стабильной самооценки")).perform()
        wd.find_element_by_link_text("7 условий стабильной самооценки").click()
        ActionChains(wd).move_to_element(wd.find_element_by_css_selector("video.video-stream.html5-main-video")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_id("watch7-user-header")).perform()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
