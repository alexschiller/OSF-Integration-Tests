from Login import Login
import pytest
import time
from selenium import webdriver


@pytest.yield_fixture
def driver():
    driver = webdriver.Remote(command_executor='http://shikhadubey1:Mhtt1XkQq18k8nqQzsqn@hub.browserstack.com:80/wd/hub',
    desired_capabilities=DesiredCapabilities.FIREFOX)
    yield driver
    driver.quit()
    
def test_login(driver):
  Login(driver)
