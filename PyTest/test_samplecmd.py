# Test has to be performed in the command window with the below commands:
# 1. pytest
# 2. py.test
# 3. pytest -v
# 4. pytest <filename.py> example: pytest test_sampleplain.py
# 5. python -m <directory name>. This runs all the test in that directories folders and sub-folders. Example: pytest -m pytest

from selenium import webdriver
import pytest

def test_setup():
    global driver
    driver = webdriver.Chrome("D:/Madhu Chandra K/Software Testing/Test Automation/chromedriver.exe")
    driver.implicitly_wait(10)
    driver.maximize_window()

def test_login():
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.find_element_by_name("txtUsername").send_keys("Admin")
    driver.find_element_by_name("txtPassword").send_keys("admin123")
    driver.find_element_by_name("Submit").click()
    var = driver.title
    assert var == "OrangeHRM"

def test_teardown():
    driver.close()
    driver.quit()
    print("Login Successful")