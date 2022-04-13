#test_Orangehrm
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from time import sleep
#ryt

class Test_OrangeHRM():

    @pytest.fixture()
    def setup(self):
        self.driver=webdriver.Chrome(executable_path=r"C:\\PythonUnitTestProject_POMBased\\drivers\\chromedriver.exe")
        self.driver.maximize_window()
        yield
        self.driver.close()

    def test_homepage(self,setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        assert self.driver.title =="OrangeHRM"

    def test_login(self,setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element(By.NAME,"txtUsername").send_keys("Admin")
        self.driver.find_element(By.NAME,"txtPassword").send_keys("admin123")
        self.driver.find_element(By.NAME,"Submit").click()
        assert self.driver.title=="OrangeHRM"