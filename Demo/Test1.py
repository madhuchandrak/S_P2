import time

from selenium import webdriver

# driver = webdriver.Chrome("D:\\Madhu Chandra K\\Software Testing\\Test Automation\\chromedriver.exe")

driver = webdriver.Chrome("D:/Madhu Chandra K/Software Testing/Test Automation/chromedriver.exe")

driver.set_page_load_timeout(10)

driver.get("https://www.google.de")

#driver.find_element_by_name("q").send_keys("Automation step by step")

#driver.find_element_by_name("btnk").click()

time.sleep(2)

driver.close()

driver.quit()

print("Test Completed")

#C:\Users\Madhu\Desktop\chromedriver.exe