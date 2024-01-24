from selenium.webdriver.support.wait import WebDriverWait

from Data import data
from Locators import locators
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager


class Base:
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    def start(self):
        self.driver.maximize_window()
        self.driver.get(data.Web_Data().url)
        self.driver.implicitly_wait(10)

    def forgotpass(self):
        self.driver.get(data.Web_Data.url)
        self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.forgotpass_locator).click()
        self.driver.get(data.Web_Data.reseturl)
        self.driver.implicitly_wait(30)
        self.driver.find_element(by=By.NAME, value=locators.Web_Locators.name).send_keys(data.Web_Data.username)
        self.driver.implicitly_wait(30)
        self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.resetbtn).click()
        output = self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.message)
        finalmessage = output.text
        print(finalmessage)


if __name__ == '__main__':
    base = Base()
    base.start()
    base.forgotpass()
