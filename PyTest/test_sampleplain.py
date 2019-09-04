
# Test starts when clicking Run (Shift+F10)
# File name should either be test_<some name>.py or <some name>_test.py. Example: test_sampleplain.py

from selenium import webdriver

driver = webdriver.Chrome("D:/Madhu Chandra K/Software Testing/Test Automation/chromedriver.exe")
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element_by_name("txtUsername").send_keys("Admin")
driver.find_element_by_name("txtPassword").send_keys("admin123")
driver.find_element_by_name("Submit").click()

driver.close()
driver.quit()
print("Login Successful")