# Using Class. Class name should start with Test<some name>. Upper case "T". Example: TestSample

from selenium import webdriver
import pytest

class TestSample():
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome("D:/Madhu Chandra K/Software Testing/Test Automation/chromedriver.exe")
        driver.implicitly_wait(10)
        driver.maximize_window()
        yield
        driver.close()
        driver.quit()
        print("Login Successful")

    def test_login(self,test_setup):
        driver.get("https://opensource-demo.orangehrmlive.com/")
        driver.find_element_by_name("txtUsername").send_keys("Admin")
        driver.find_element_by_name("txtPassword").send_keys("admin123")
        driver.find_element_by_name("Submit").click()
        var = driver.title
        assert var == "OrangeHRM"