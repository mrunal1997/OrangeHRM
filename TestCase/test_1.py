import pytest
from time import sleep
from src.LoginPage import Login
from src.DashBoard import Dashboard
from src.UserMAnagement import UserMAnagement
import configparser
parser = configparser.ConfigParser()
parser.read(filenames="TestCase/inputs.properties")

@pytest.mark.usefixtures("webPage")
class Test_login:

    def test_login(self):
        login = Login(self.driver)
        dashboard = Dashboard(self.driver)
        sleep(2)
        login.username(parser.get("correct_credential", "username"))
        login.password(parser.get("correct_credential", "password"))
        login.click_logIn()
        sleep(3)
        if "Dashboard" in dashboard.isTitle():
            assert True
        else:
            assert False, "Title not found...!!!"

    def test_invalid_inputs(self):
        login = Login(self.driver)
        sleep(2)
        login.username(parser.get("incorrect_credential", "username1"))
        login.password(parser.get("incorrect_credential", "password1"))
        login.click_logIn()
        sleep(3)
        if "Invalid credentials" in login.invalid_msg():
            assert True
        else:
            assert False, "Text not found...!!!"

    def test_db_list(self):
        login = Login(self.driver)
        dashboard = Dashboard(self.driver)
        sleep(2)
        login.username(parser.get("correct_credential", "username"))
        login.password(parser.get("correct_credential", "password"))
        login.click_logIn()
        sleep(3)
        dashboard.click_admin()
        sleep(3)
        dashboard.admin_add_usr()
        sleep(3)
        dashboard.admin_user_role()
        sleep(3)
        dashboard.admin_status()
        sleep(3)
        dashboard.emp_name(parser.get("emp_data", "name"))
        sleep(2)
        dashboard.emp_usrname(parser.get("emp_data", "usrname"))
        sleep(2)
        dashboard.emp_pswrd(parser.get("emp_data", "pswrd"))
        sleep(2)
        dashboard.emp_cfpwd(parser.get("emp_data", "cfpswrd"))
        sleep(2)
        dashboard.click_save()
        sleep(2)

    def test_um_search_emp(self):
        login = Login(self.driver)
        usr_mngmt = UserMAnagement(self.driver)
        dashboard = Dashboard(self.driver)
        sleep(2)
        login.username(parser.get("correct_credential", "username"))
        login.password(parser.get("correct_credential", "password"))
        login.click_logIn()
        sleep(3)
        dashboard.click_admin()
        sleep(2)
        usr_mngmt.sys_usr_Usrnm(parser.get("emp_data", "usrname"))
        sleep(2)
        usr_mngmt.sys_usr_usr_Role()
        sleep(2)
        usr_mngmt.sys_usr_emp_Name()
        sleep(2)
        usr_mngmt.sys_usr_emp_Status()
        sleep(2)
        usr_mngmt.click_search()
        sleep(2)
        if "(1) Record Found" in usr_mngmt.sys_usr_emp_record_found():
            assert True
        else:
            assert False