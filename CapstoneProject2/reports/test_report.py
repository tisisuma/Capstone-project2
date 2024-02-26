from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from Data import data
from Locators import locators


class Test_OrangeHRM:

    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        yield
        self.driver.close()

    def test_get_title(self, booting_function):
        self.driver.get(data.Web_Data.url)
        self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.forgotpass_locator).click()
        assert self.driver.current_url == data.Web_Data.reseturl
        print("{a} SUCCESS : Web Title Verified".format(a=data.Web_Data().reseturl))

    def test_forgotpass(self, booting_function):
        self.driver.get(data.Web_Data.reseturl)
        self.driver.implicitly_wait(30)
        self.driver.find_element(by=By.NAME, value=locators.Web_Locators.name).send_keys(data.Web_Data.username)
        self.driver.implicitly_wait(30)
        self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.resetbtn).click()
        output = self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.message)
        finalmessage = output.text
        assert finalmessage == data.Web_Data.Confirmmessage
        print("Success : Password reset done {b}".format(b=data.Web_Data.Confirmmessage))

    def test_module(self, booting_function):
        self.driver.get(data.Web_Data().url)
        self.driver.find_element(by=By.NAME, value=locators.Web_Locators().username_locator).send_keys(
            data.Web_Data().username1)
        self.driver.find_element(by=By.NAME, value=locators.Web_Locators().password_locator).send_keys(
            data.Web_Data().password1)
        self.driver.find_element(by=By.XPATH, value=locators.Web_Locators().submit_button_locator).click()
        self.driver.implicitly_wait(10)

        assert self.driver.current_url == data.Web_Data().dashboardurl
        print("SUCCESS : Logged in with Username {a} & Password {b}".format(a=data.Web_Data().username,
                                                                            b=data.Web_Data.password1))
        self.driver.implicitly_wait(3)

        if self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.admin_locator).is_displayed():
            self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.admin_locator).click()
            assert self.driver.current_url == data.Web_Data.adminurl
            print("Admin Module Available", self.driver.current_url)
        else:
            print("Admin Module not present")
        self.driver.implicitly_wait(3)

        if self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.usermanagement_locator).is_displayed():
            self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.usermanagement_locator).click()
            print("User Management Module Available")
        else:
            print("User Management Module not present")

        if self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.job_locator).is_displayed():
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
        self.driver.quit()

    def test_adminmodule(self, booting_function):
        self.driver.get(data.Web_Data().url)
        self.driver.find_element(by=By.NAME, value=locators.Web_Locators().username_locator).send_keys(
            data.Web_Data().username1)
        self.driver.find_element(by=By.NAME, value=locators.Web_Locators().password_locator).send_keys(
            data.Web_Data().password1)
        self.driver.find_element(by=By.XPATH, value=locators.Web_Locators().submit_button_locator).click()
        self.driver.implicitly_wait(10)

        assert self.driver.current_url == data.Web_Data().dashboardurl
        print("SUCCESS : Logged in with Username {a} & Password {b}".format(a=data.Web_Data().username,
                                                                            b=data.Web_Data.password1))

        if self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.admin_locator).is_displayed():
            self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.admin_locator).click()
            assert self.driver.current_url == data.Web_Data.adminurl
            print("Admin Module Available", self.driver.current_url)
        else:
            print("Admin Module not present")

        if self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.pim_locator).is_displayed():
            self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.pim_locator).click()
            assert self.driver.current_url == data.Web_Data.pimurl
            print("PIM Module Available", self.driver.current_url)
        else:
            print("PIM Module not present")

        if self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.leave_locator).is_displayed():
            self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.leave_locator).click()
            assert self.driver.current_url == data.Web_Data.leaveurl
            print("Leave Module Available", self.driver.current_url)
        else:
            print("Leave Module not present")

        if self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.time_locator).is_displayed():
            self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.time_locator).click()
            assert self.driver.current_url == data.Web_Data.timeurl
            print("Time Module Available", self.driver.current_url)
        else:
            print("Time Module not present")

        if self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.recruitment_locator).is_displayed():
            self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.recruitment_locator).click()
            assert self.driver.current_url == data.Web_Data.recruitmenturl
            print("Recruitment Module Available", self.driver.current_url)
        else:
            print("Recruitment Module not present")

        if self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.myinfo_locator).is_displayed():
            self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.myinfo_locator).click()
            assert self.driver.current_url == data.Web_Data.myinfo
            print("MyInfo Module Available", self.driver.current_url)
        else:
            print("MyInfo Module not present")

        if self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.performance_locator).is_displayed():
            self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.performance_locator).click()
            assert self.driver.current_url == data.Web_Data.performanceurl
            print("Performance Module Available", self.driver.current_url)
        else:
            print("Performance Module not present")

        if self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.dashboard_locator).is_displayed():
            self.driver.implicitly_wait(3)
            self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.dashboard_locator).click()
            assert self.driver.current_url == data.Web_Data.dashboardurl
            print("Dashboard Module Available", self.driver.current_url)
        else:
            print("Dashboard Module not present")

        if self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.directory_locator).is_displayed():
            self.driver.implicitly_wait(3)
            self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.directory_locator).click()
            assert self.driver.current_url == data.Web_Data.directoryurl
            print("Directory Module Available", self.driver.current_url)
        else:
            print("Directory Module not present")

        if self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.maintanence_locator).is_displayed():
            self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.maintanence_locator).click()
            self.driver.implicitly_wait(3)
            self.driver.find_element(by=By.NAME, value=locators.Web_Locators.password_locator).send_keys(
                data.Web_Data.password1)
            self.driver.find_element(by=By.XPATH, value=locators.Web_Locators().confirmbutton_locator).click()
            self.driver.implicitly_wait(3)
            assert self.driver.current_url == data.Web_Data.maintanenceurl
            print("Maintenance Module Available", self.driver.current_url)
        else:
            print("Maintenance Module not present")

        if self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.claim_locator).is_displayed():
            self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.claim_locator).click()
            assert self.driver.current_url == data.Web_Data.claimurl
            print("Claim Module Available", self.driver.current_url)
        else:
            print("Claim Module not present")

        if self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.buzz_locator).is_displayed():
            self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.buzz_locator).click()
            assert self.driver.current_url == data.Web_Data.buzzurl
            print("Buzz Module Available", self.driver.current_url)
        else:
            print("Buzz Module not present")

        print("SUCCESS : All Modules available")
        self.driver.quit()
