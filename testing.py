import time
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(2)
driver.find_element("name", "username").send_keys("admin")
driver.find_element("name", "password").send_keys("admin123")
driver.find_element("xpath", "//button[normalize-space()='Login']").click()
time.sleep(3)
driver.find_element("xpath", "//ul[@class='oxd-main-menu']/li[1]").click()
time.sleep(2)
driver.find_element("xpath", "//button[normalize-space()='Add']").click()

dropdown = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]"))
)
dropdown.click()

option_to_select = WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.XPATH, "//div[@role='listbox']/div[1]"))
)
option_to_select.click()
# driver.find_element("xpath", "//button[normalize-space()='Add']").click()
# time.sleep(2)
# driver.find_element("xpath", "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]").click()
# time.sleep(2)
# driver.find_element("xpath", "//div[@role='listbox'][@class='oxd-select-dropdown --position-bottom'][1]").click()
