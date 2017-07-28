from Login import Login
import pytest
import time
from selenium import webdriver


'''@pytest.yield_fixture
def driver():
    desired_cap= {'browser': 'Chrome', 'browser_version': '59.0', 'os': 'Windows', 'os_version': '10', 'resolution': '1024x768'}
    driver= webdriver.Remote(
    command_executor='http://shikhadubey1:Mhtt1XkQq18k8nqQzsqn@hub.browserstack.com:80/wd/hub',
    desired_capabilities= desired_cap)
    yield driver
    driver.quit()'''

desired_cap= {'browser': 'Chrome', 'browser_version': '59.0', 'os': 'Windows', 'os_version': '10', 'resolution': '1024x768'}
driver= webdriver.Remote(
command_executor='http://shikhadubey1:Mhtt1XkQq18k8nqQzsqn@hub.browserstack.com:80/wd/hub',
desired_capabilities= desired_cap)

class idontknow:
    def test_login(driver):
        
        driver.get("https://staging.osf.io/")
        time.sleep(3)
        driver.find_element_by_partial_link_text("Sign In").click()
        time.sleep(3)
        driver.find_element_by_id("username").send_keys("shkd28892@gmail.com")
        time.sleep(3)
        driver.find_element_by_id('password').send_keys('Shikh@28892')
        time.sleep(3)
        driver.implicitly_wait(10)
        if (driver.find_element_by_id("rememberMe").is_selected()):
            driver.find_element_by_id("rememberMe").click()

        driver.find_element_by_name("submit").click()
        driver.quit()
