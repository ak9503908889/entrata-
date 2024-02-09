import pytest


@pytest.mark.usefixtures("setup_and_teardown","log_on_failure")
class BaseTest:
    pass

    # #  log_on_failure is the screenshot taking method in conftest file
    #
    #
    #
    #
    #   """for access data for execel we need to install openpyxl extention
    #
    # # for allure report install node.js
    # #ninstall allure commandline type on cmd===  npm install -g allure-commandline
    # # check==   allure --version
    #
    # # pip install allure-pytest
    # # for genrate allure report == pytest --alluredir="./reports"
    #
    # for open json report go to main project right click open in
    # explorer open project location select path and type cmd enter then type on cmd== allure serve "./reports"
    #  """