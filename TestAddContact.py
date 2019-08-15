# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_add_contact(self):
        driver = self.driver
        driver.get("http://localhost/addressbook/group.php")
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys("admin")
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys("secret")
        driver.find_element_by_xpath("//input[@value='Login']").click()
        driver.find_element_by_link_text("add new").click()
        driver.find_element_by_name("firstname").clear()
        driver.find_element_by_name("firstname").send_keys("test")
        driver.find_element_by_name("middlename").clear()
        driver.find_element_by_name("middlename").send_keys("test")
        driver.find_element_by_name("lastname").clear()
        driver.find_element_by_name("lastname").send_keys("test")
        driver.find_element_by_name("nickname").clear()
        driver.find_element_by_name("nickname").send_keys("test001")
        driver.find_element_by_name("title").clear()
        driver.find_element_by_name("title").send_keys("title test")
        driver.find_element_by_name("company").clear()
        driver.find_element_by_name("company").send_keys("company test")
        driver.find_element_by_name("address").clear()
        driver.find_element_by_name("address").send_keys("address test")
        driver.find_element_by_name("home").clear()
        driver.find_element_by_name("home").send_keys("00000000")
        driver.find_element_by_name("mobile").clear()
        driver.find_element_by_name("mobile").send_keys("00000000")
        driver.find_element_by_name("work").clear()
        driver.find_element_by_name("work").send_keys("00000000")
        driver.find_element_by_name("fax").clear()
        driver.find_element_by_name("fax").send_keys("00000000")
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("test1@email.net")
        driver.find_element_by_name("email2").clear()
        driver.find_element_by_name("email2").send_keys("test2@email.net")
        driver.find_element_by_name("email3").clear()
        driver.find_element_by_name("email3").send_keys("test3@email.net")
        driver.find_element_by_name("homepage").clear()
        driver.find_element_by_name("homepage").send_keys("homepage_test.net")
        Select(driver.find_element_by_name("bday")).select_by_visible_text("29")
        driver.find_element_by_xpath("//option[@value='29']").click()
        Select(driver.find_element_by_name("bmonth")).select_by_visible_text("June")
        driver.find_element_by_xpath("//option[@value='June']").click()
        driver.find_element_by_name("byear").clear()
        driver.find_element_by_name("byear").send_keys("1995")
        Select(driver.find_element_by_name("aday")).select_by_visible_text("29")
        driver.find_element_by_xpath("(//option[@value='29'])[2]").click()
        Select(driver.find_element_by_name("amonth")).select_by_visible_text("June")
        driver.find_element_by_xpath("(//option[@value='June'])[2]").click()
        driver.find_element_by_name("ayear").clear()
        driver.find_element_by_name("ayear").send_keys("1995")
        Select(driver.find_element_by_name("new_group")).select_by_visible_text("test")
        driver.find_element_by_xpath("(//option[@value='4'])[3]").click()
        driver.find_element_by_name("address2").clear()
        driver.find_element_by_name("address2").send_keys("address test")
        driver.find_element_by_name("phone2").clear()
        driver.find_element_by_name("phone2").send_keys("00000000")
        driver.find_element_by_name("notes").clear()
        driver.find_element_by_name("notes").send_keys("notes test")
        driver.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        driver.find_element_by_link_text("Logout").click()
    
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
