from selenium import webdriver
# from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import pytest
from Data import data
from Locators import locators


class Test_OrangeHRM:

    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        # self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        yield
        self.driver.close()

    def test_get_title(self, booting_function):
        self.driver.get(data.Web_Data().url)
        assert self.driver.current_url == data.Web_Data.url
        print("SUCCESS : Web Title Verified")

    def test_login(self, booting_function):
        self.driver.get(data.Web_Data().url)
        self.driver.find_element(by=By.NAME, value=locators.Web_Locators().username_locator).send_keys(
            data.Web_Data().username)
        self.driver.find_element(by=By.NAME, value=locators.Web_Locators().password_locator).send_keys(
            data.Web_Data().password)
        self.driver.find_element(by=By.XPATH, value=locators.Web_Locators().submit_button_locator).click()
        self.driver.implicitly_wait(10)


        assert self.driver.current_url == data.Web_Data().dashboardurl
        print("SUCCESS : Logged in with Username {a} & Password {b}".format(a=data.Web_Data().username,
                                                                            b=data.Web_Data.password))
        self.driver.implicitly_wait(3)

        if self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.admin_locator).is_displayed():
            self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.admin_locator).click()
            assert self.driver.current_url == data.Web_Data.adminurl
            print("Admin Module Available",self.driver.current_url)
        else:
            print("Admin Module not present")
        self.driver.implicitly_wait(3)

        if self.driver.find_element(by=By.XPATH,value=locators.Web_Locators.usermanagement_locator).is_displayed():
            self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.usermanagement_locator).click()
            print("User Management Module Available")
        else:
            print("User Management Module not present")


        if self.driver.find_element(by=By.XPATH,value=locators.Web_Locators.job_locator).is_displayed():
            self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.job_locator).click()
            print("Job Module Available")
        else:
            print("Job Module not present")

        if self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.org_locator).is_displayed():
            self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.org_locator).click()
            print("Organization Module Available")
        else:
            print("Organization Module not present")

        if self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.qualification_locator).is_displayed():
            self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.qualification_locator).click()
            print("Qualification Module Available")
        else:
            print("Qualification Module not present")

        if self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.nationality_locator).is_displayed():
            self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.nationality_locator).click()
            print("Nationality Module Available")
        else:
            print("Nationality Module not present")

        if self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.corporatebanking_locator).is_displayed():
            self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.corporatebanking_locator).click()
            print("Corporate Banking Module Available", self.driver.current_url)
        else:
            print("Corporate Banking not present")

        if self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.configuration_locator).is_displayed():
            self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.configuration_locator).click()
            print("Configuration Module Available", self.driver.current_url)
        else:
            print("Configuration Module not present")



        print("SUCCESS : All Modules available")









