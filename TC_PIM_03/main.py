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
        print("Admin Module Available", self.driver.current_url)


        self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.pim_locator).click()
        print("PIM Module Available", self.driver.current_url)


        self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.leave_locator).click()
        print("Leave Module Available", self.driver.current_url)


        self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.time_locator).click()
        print("Time Module Available", self.driver.current_url)


        self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.recruitment_locator).click()
        print("Recruitment Module Available", self.driver.current_url)


        self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.myinfo_locator).click()
        print("MyInfo Module Available", self.driver.current_url)


        self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.performance_locator).click()
        print("Performance Module Available", self.driver.current_url)


        self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.dashboard_locator).click()
        print("Dashboard Module Available", self.driver.current_url)


        self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.directory_locator).click()
        print("Directory Module Available", self.driver.current_url)


        self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.maintanence_locator).click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(by=By.NAME, value=locators.Web_Locators.password_locator).send_keys(
            data.Web_Data.password)
        self.driver.find_element(by=By.XPATH, value=locators.Web_Locators().confirmbutton_locator).click()
        self.driver.implicitly_wait(3)

        print("Maintenance Module Available", self.driver.current_url)



        self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.claim_locator).click()
        print("Claim Module Available", self.driver.current_url)


        self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.buzz_locator).click()
        print("Buzz Module Available", self.driver.current_url)
        self.driver.quit()


    print("SUCCESS : All Modules available")

if __name__ == '__main__':
    base = Base()
    base.start()
    base.login()
    base.module()
