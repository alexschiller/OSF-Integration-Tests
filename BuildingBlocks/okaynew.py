from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from threading import Thread
import time#
from selenium.webdriver.support.select import Select
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class Login:
   
    def test_login(self, driver):
        
        driver.get("https://osf.io/")
        time.sleep(3)
        driver.find_element_by_partial_link_text("Sign In").click()
        time.sleep(3)
        driver.find_element_by_id("username").send_keys("osframeworktesting+ghost@gmail.com")
        time.sleep(3)
        driver.find_element_by_id('password').send_keys('\"Repr0duce!\"')
        time.sleep(3)
        driver.implicitly_wait(10)
        if (driver.find_element_by_id("rememberMe").is_selected()):
            driver.find_element_by_id("rememberMe").click()
                
        driver.find_element_by_name("submit").click()
        
def test_CreateProject(self, driver):
        time.sleep(3)
        driver.find_element_by_css_selector("#osfHome > div.quickSearch > div > div > div > div > div:nth-child(1) > m-b-lg > div > span > button").click()
        time.sleep(3)
        driver.find_element_by_name("projectName").send_keys("Testselenium")
        time.sleep(3)
        driver.find_element_by_css_selector("#addProjectFromHome > div > div > div.modal-footer > button.btn.btn-success").click()
        time.sleep(3)
        driver.find_element_by_css_selector("#addProjectFromHome > div > div > div > div.modal-footer > a").click()
        
