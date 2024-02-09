import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver

from Utilities import ReadConfigurations


@pytest.fixture()    # this method is use for attach screenshot to allure report only fail test.
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="failed_test",
                      attachment_type=AttachmentType.PNG)

## this method is use for attch screenshot to allure report only fail test.
## only give the above method name in base test so applicable for all tests
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture
def setup_and_teardown(request):
    browser=ReadConfigurations.read_configuration("basic info","browser")
    global driver
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