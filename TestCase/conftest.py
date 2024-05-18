from selenium import webdriver
import pytest
import configparser
parser = configparser.ConfigParser()
parser.read(filenames="TestCase/inputs.properties")

@pytest.fixture
def webPage(request):
    request.cls.driver = webdriver.Chrome()
    request.cls.driver.get(parser.get("Url", "page_url"))
    request.cls.driver.maximize_window()
    # yield
    # request.cls.driver.quit()

# def pytest_html_repoMy Selenium web application testing!"rt_title(report):
# #     report.title = "
