from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
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
        # self.driver.close()

    def test_get_title(self, booting_function):
        self.driver.get(data.Web_Data.url)
        self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.forgotpass_locator).click()
        assert self.driver.current_url == data.Web_Data.reseturl
        print("{a} SUCCESS : Web Title Verified".format(a=data.Web_Data().reseturl))

    def test_forgotpass(self,booting_function):
        self.driver.get(data.Web_Data.reseturl)
        self.driver.implicitly_wait(30)
        self.driver.find_element(by=By.NAME, value=locators.Web_Locators.name).send_keys(data.Web_Data.username)
        self.driver.implicitly_wait(30)
        self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.resetbtn).click()
        output = self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.message)
        finalmessage = output.text
        assert finalmessage == data.Web_Data.Confirmmessage
        print("Success : Password reset done {b}".format(b=data.Web_Data.Confirmmessage))





