from selenium.webdriver.firefox.webdriver import WebDriver

class Application:
    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def Open_home_page(self):
        wd = self.wd
        wd.get("https://my.textmagic.com/login")

    def login(self, username, password):
            wd = self.wd

            self.Open_home_page()
            wd.find_element_by_id("_username").click()
            wd.find_element_by_id("_username").clear()
            wd.find_element_by_id("_username").send_keys(username)
            wd.find_element_by_id("_username").click()
            wd.find_element_by_id("_password").click()
            wd.find_element_by_id("_password").clear()
            wd.find_element_by_id("_password").send_keys(password)
            wd.find_element_by_id("_password").click()
            wd.find_element_by_id("logInBtn").click()

    def create_template(self, group):
                wd = self.wd

                wd.find_element_by_link_text("Templates").click()
                wd.find_element_by_link_text("New template").click()
                wd.find_element_by_id("addListName").click()
                wd.find_element_by_id("addListName").clear()
                wd.find_element_by_id("addListName").send_keys(group.listname)
                wd.find_element_by_id("addListName").click()
                wd.find_element_by_id("editTmplText").click()
                wd.find_element_by_id("editTmplText").clear()
                wd.find_element_by_id("editTmplText").send_keys(group.Tmptext)
                wd.find_element_by_id("editTmplText").click()
                wd.find_element_by_id("addTemplateBtn").click()

    def destroy(self):
        self.wd.quit()