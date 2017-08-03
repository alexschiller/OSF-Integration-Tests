'''
Created on Jun 14, 2017

@author: shikhadubey
'''
import time#

class CreateProject:

    def __init__(self, driver):
        time.sleep(3)
        driver.find_element_by_css_selector("#osfHome > div.quickSearch > div > div > div > div > div:nth-child(1) > m-b-lg > div > span > button").click()
        time.sleep(3)
        driver.find_element_by_name("projectName").send_keys("Testselenium")
        time.sleep(3)
        driver.find_element_by_css_selector("#addProjectFromHome > div > div > div.modal-footer > button.btn.btn-success").click()
        time.sleep(3)
        driver.find_element_by_css_selector("//*[@id='addProjectFromHome']/div/div/div/div[2]/a").click()
        
