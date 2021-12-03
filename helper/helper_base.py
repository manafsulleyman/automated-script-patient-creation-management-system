from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class HelperFunc(object):

    base_url = 'http://localhost:3000/'
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)

    def open(self):
        self.driver.get(self.base_url)

    def maximize(self):
        self.driver.maximize_window()

    def close(self):
        self.driver.quit()

    def find_by_xpath(self, xpath):
        return self.driver.find_element_by_xpath(xpath)

    # def find_by_name(self, name):
    #     return self.driver.find_element_by_name(name)



