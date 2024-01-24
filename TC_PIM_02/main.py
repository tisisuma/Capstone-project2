from Data import data
from Locators import locators
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.common.exceptions import NoSuchElementException


class Base:
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    def start(self):
        self.driver.maximize_window()
        self.driver.get(data.Web_Data().url)
        self.driver.implicitly_wait(10)

    def login(self):
        try:
            self.driver.find_element(by=By.NAME, value=locators.Web_Locators().username_locator).send_keys(
                data.Web_Data().username)
            self.driver.find_element(by=By.NAME, value=locators.Web_Locators().password_locator).send_keys(
                data.Web_Data().password)
            self.driver.find_element(by=By.XPATH, value=locators.Web_Locators().submit_button_locator).click()
            print("Login Successfully")
        except NoSuchElementException as e:
            print("Error : ", e)

    def module(self):


        self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.admin_locator).click()
        print("Admin Module Available")


        self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.usermanagement_locator).click()
        print("User Management Module Available")


        self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.job_locator).click()
        print("Job Module Available")


        self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.org_locator).click()
        print("Organization Module Available")


        self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.qualification_locator).click()
        print("Qualification Module Available")


        self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.nationality_locator).click()
        print("Nationality Module Available")


        self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.corporatebanking_locator).click()
        print("Corporate Branding Module Available")


        self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.configuration_locator).click()
        print("Configuration Module Available")
        self.driver.quit()

        print("SUCCESS : All Modules available")

if __name__ == '__main__':
    base = Base()
    base.start()
    base.login()
    base.module()
