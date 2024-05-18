class Login:

    def __init__(self, driver):

        super().__init__()
        self.driver = driver
        self.xpath_username = "username"
        self.xpath_password = "password"
        self.xpath_logInBtn = "//button[normalize-space()='Login']"
        self.xpath_invalidMsg = "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']"
        # self.logger = LogClass().get_logger()

    def username(self, username):
        # logger = self.getLogs()
        self.driver.find_element("name", self.xpath_username).send_keys(username)
        # logger.info("Login with username: %s", username)

    def password(self, password):
        self.driver.find_element("name", self.xpath_password).send_keys(password)
        # logger.info("Login with username: %s", password)

    def click_logIn(self):
        self.driver.find_element("xpath", self.xpath_logInBtn).click()

    def invalid_msg(self):
        # logger.error("Error: Invalid credentials")
        return self.driver.find_element("xpath", self.xpath_invalidMsg).text