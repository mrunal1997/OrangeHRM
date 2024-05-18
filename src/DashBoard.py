from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Dashboard:
    def __init__(self, driver):

        super().__init__()
        self.driver = driver
        self.xpath_title = "//h6[normalize-space()='Dashboard']"
        self.xpath_admin = "//ul[@class='oxd-main-menu']/li[1]"
        self.xpath_add_user = "//button[normalize-space()='Add']"
        self.xpath_user_role = "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]"
        self.xpath_user_role_opt = "//div[@role='listbox']/div[2]"
        self.xpath_status = "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]"
        self.xpath_status_opt = "//div[@role='listbox']//div[2]"
        self.xpath_emp_name = "//input[@placeholder='Type for hints...']"
        self.xpath_suggession = "//span[normalize-space()='MUKESH CHANDRA BALODI']"
        self.xpath_emp_username = "//div[@class='oxd-form-row']//div[@class='oxd-grid-2 orangehrm-full-width-grid']//div[@class='oxd-grid-item oxd-grid-item--gutters']//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@class='oxd-input oxd-input--active']"
        self.xpath_emp_password = "//div[@class='oxd-grid-item oxd-grid-item--gutters user-password-cell']//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@type='password']"
        self.xpath_emp_cfpassword = "//div[@class='oxd-grid-item oxd-grid-item--gutters']//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@type='password']"
        self.xpath_save_btn = "//button[normalize-space()='Save']"
    def isTitle(self):
        return self.driver.find_element("xpath", self.xpath_title).text

    def click_admin(self):
        self.driver.find_element("xpath", self.xpath_admin).click()

    def admin_add_usr(self):
        self.driver.find_element("xpath", self.xpath_add_user).click()

    def admin_user_role(self):
        dropdown = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, self.xpath_user_role)))
        dropdown.click()
        option_to_select = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, self.xpath_user_role_opt))
        )
        option_to_select.click()

    def admin_status(self):
        dropdown = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, self.xpath_status)))
        dropdown.click()
        option_to_select = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, self.xpath_status_opt))
        )
        option_to_select.click()

    def emp_name(self, emp_name):
        ddropdown = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, self.xpath_emp_name)))
        ddropdown.send_keys(emp_name)
        option_to_select = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, self.xpath_suggession))
        )
        option_to_select.click()

    def emp_usrname(self, emp_usrname):
        self.driver.find_element("xpath", self.xpath_emp_username).send_keys(emp_usrname)

    def emp_pswrd(self, emp_pswd):
        self.driver.find_element("xpath", self.xpath_emp_password).send_keys(emp_pswd)

    def emp_cfpwd(self, emp_pswd):
        self.driver.find_element("xpath", self.xpath_emp_cfpassword).send_keys(emp_pswd)

    def click_save(self):
        self.driver.find_element("xpath", self.xpath_save_btn).click()