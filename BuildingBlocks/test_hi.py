from Login import test_login
from Login import test_CreateProject
import pytest
import time
from selenium import webdriver


@pytest.yield_fixture
def driver():
    desired_cap = {'browser': 'Safari', 'browser_version': '10.1', 'os': 'OS X', 'os_version': 'Sierra', 'resolution': '1024x768'}
    driver= webdriver.Remote(
    command_executor='http://shikhadubey1:Mhtt1XkQq18k8nqQzsqn@hub.browserstack.com:80/wd/hub',
    desired_capabilities= desired_cap)
    yield driver
    driver.quit()
    
def test_login(driver):
    test_login(driver)
    test_CreateProject(driver)
