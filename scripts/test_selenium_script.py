# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class NewChatAppln(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_new_chat_appln(self):
        driver = self.driver
        driver.get("http://${TARGET_HOST}:${TARGET_PORT}/login#")
        driver.find_element_by_link_text("Account for External User").click()
        driver.find_element_by_id("username").click()
        driver.find_element_by_id("username").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("demousr1")
        driver.find_element_by_id("email").click()
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("demousr1@wipro.com")
        driver.find_element_by_id("display-name").click()
        driver.find_element_by_id("display-name").clear()
        driver.find_element_by_id("display-name").send_keys("demousr1")
        driver.find_element_by_id("first-name").click()
        driver.find_element_by_id("first-name").clear()
        driver.find_element_by_id("first-name").send_keys("firstname")
        driver.find_element_by_id("last-name").click()
        driver.find_element_by_id("last-name").click()
        driver.find_element_by_id("last-name").clear()
        driver.find_element_by_id("last-name").send_keys("lastname")
        driver.find_element_by_xpath("//div[5]").click()
        driver.find_element_by_id("password").click()
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("wipro@123")
        driver.find_element_by_id("password-confirm").click()
        driver.find_element_by_id("password-confirm").clear()
        driver.find_element_by_id("password-confirm").send_keys("wipro@123")
        driver.find_element_by_id("submit").click()
        #driver.find_element_by_css_selector("button.confirm").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()