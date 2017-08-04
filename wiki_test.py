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

class wiki_test(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_wiki_test(self):
        success = True
        wd = self.wd
        wd.get("https://uk.wikipedia.org/wiki/%D0%93%D0%BE%D0%BB%D0%BE%D0%B2%D0%BD%D0%B0_%D1%81%D1%82%D0%BE%D1%80%D1%96%D0%BD%D0%BA%D0%B0")
        ActionChains(wd).move_to_element(wd.find_element_by_xpath("//div[@class='mw-parser-output']//div[.='Ласкаво просимо до Вікіпедії,']")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_xpath("//div[@class='mw-parser-output']/div/div[1]/table/tbody/tr/td[1]")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_xpath("//div[@class='mw-parser-output']/div/p")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_css_selector("span.frb-inline-close-bottom-wrapper")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_id("mw-content-text")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_css_selector("div.frb-inline-main")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_css_selector("button.frb-btn.frb-btn-logo")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_css_selector("div.frb-inline-message")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_css_selector("div.frb-inline-main")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_css_selector("div.frb-inline-topbar")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_id("frb-inline")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_id("bodyContent")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_id("content")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_id("searchInput")).perform()
        wd.find_element_by_id("searchInput").click()
        wd.find_element_by_id("searchInput").clear()
        wd.find_element_by_id("searchInput").send_keys("byce")
        ActionChains(wd).move_to_element(wd.find_element_by_id("simpleSearch")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_id("searchButton")).perform()
        wd.find_element_by_id("searchInput").click()
        wd.find_element_by_id("searchInput").send_keys("\\undefined")
        wd.find_element_by_id("searchButton").click()
        ActionChains(wd).move_to_element(wd.find_element_by_id("searchInput")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_id("content")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_id("firstHeading")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_id("bodyContent")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_id("search")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_css_selector("div.mw-search-profile-tabs")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_xpath("//div[@id='mw-content-text']/div[1]")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_id("mw-content-text")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_css_selector("p.mw-search-createlink")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_link_text("сторінки, що починаються з цієї назви")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_css_selector("p.mw-search-createlink")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_id("mw-content-text")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_xpath("//div[@id='mw-content-text']/div[1]")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_css_selector("div.mw-search-profile-tabs")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_link_text("Мультимедіа")).perform()
        wd.find_element_by_link_text("Мультимедіа").click()
        ActionChains(wd).move_to_element(wd.find_element_by_link_text("Мультимедіа")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_css_selector("div.mw-search-profile-tabs")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_xpath("//div[@id='mw-content-text']/div[1]")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_id("mw-content-text")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_link_text("створити сторінку «Byce»")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_xpath("//ul[@class='mw-search-results']/li[1]")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_css_selector("div.searchresults")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_css_selector("div.searchresults")).perform()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
