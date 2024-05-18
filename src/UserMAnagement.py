from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UserMAnagement:
    def __init__(self, driver):

        super().__init__()
        self.driver = driver
        self.xpath_um_usrnm = "//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@class='oxd-input oxd-input--active']"
        self.xpath_um_usr_role = "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]"
        self.xpath_um_usr_role_opt = "//span[contains(text(),'Admin')]"
        self.xpath_um_emp_name = "//input[@placeholder='Type for hints...']"
        self.xpath_um_emp_name_opt = "//span[contains(text(),'Danny')]"
        self.xpath_um_status = "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[4]/div[1]/div[2]/div[1]/div[1]/div[1]"
        self.xpath_um_status_opt = "//span[normalize-space()='Enabled']"
        self.xpath_search_btn = "//button[normalize-space()='Search']"
        self.xpath_um_record_found = "//span[normalize-space()='(1) Record Found']"

    def sys_usr_Usrnm(self, sys_usr_usrname):
        self.driver.find_element("xpath", self.xpath_um_usrnm).send_keys(sys_usr_usrname)

    def sys_usr_usr_Role(self):
        dropdown = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, self.xpath_um_usr_role)))
        dropdown.click()
        option_to_select = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, self.xpath_um_usr_role_opt))
        )
        option_to_select.click()

    def sys_usr_emp_Name(self):
        dropdown = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, self.xpath_um_emp_name)))
        dropdown.send_keys("dan")
        option_to_select = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, self.xpath_um_emp_name_opt))
        )
        option_to_select.click()

    def sys_usr_emp_Status(self):
        dropdown = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, self.xpath_um_status)))
        dropdown.click()
        option_to_select = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, self.xpath_um_status_opt))
        )
        option_to_select.click()

    def click_search(self):
        self.driver.find_element("xpath", self.xpath_search_btn).click()

    def sys_usr_emp_record_found(self):
        return self.driver.find_element("xpath", self.xpath_um_record_found).text