import pytest
from selenium import webdriver

from Utilities import ReadConfigurations


@pytest.fixture
def setup_and_teardown(request):
    browser=ReadConfigurations.read_configuration("basic info","browser")
    driver=None
    if browser.__eq__("chrome"):
        driver=webdriver.Chrome()
    elif browser.__eq__("firefox"):
        driver=webdriver.Firefox()
    elif browser.__eq__("edge"):
        driver=webdriver.Edge
    else:
        print("provide a valid browser name from the list chrome/firfox/edge")


    driver.maximize_window()
    app_url=ReadConfigurations.read_configuration("basic info","url")
    driver.get(app_url)
    request.cls.driver=driver
    yield
    driver.quit()