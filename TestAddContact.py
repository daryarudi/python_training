# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from date import Date
from log import Log


class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
    
    def test_add_contact(self):
        wd = self.wd
        log = Log(wd, "http://localhost/addressbook/group.php")
        log.open_home_page()
        log.login(username="admin", password="secret")
        self.open_add_contact_page(wd)
        self.create_contact(wd)
        log.logout()

    def create_contact(self, wd):
        wd.find_element_by_name("firstname").send_keys("test")
        wd.find_element_by_name("middlename").send_keys("test")
        wd.find_element_by_name("lastname").send_keys("test")

        wd.find_element_by_name("nickname").send_keys("test001")
        wd.find_element_by_name("title").send_keys("title test")
        wd.find_element_by_name("company").send_keys("company test")
        wd.find_element_by_name("address").send_keys("address test")

        wd.find_element_by_name("home").send_keys("00000000")
        wd.find_element_by_name("mobile").send_keys("00000000")
        wd.find_element_by_name("work").send_keys("00000000")
        wd.find_element_by_name("fax").send_keys("00000000")

        wd.find_element_by_name("email").send_keys("test1@email.net")
        wd.find_element_by_name("email2").send_keys("test2@email.net")
        wd.find_element_by_name("email3").send_keys("test3@email.net")

        wd.find_element_by_name("homepage").send_keys("homepage_test.net")

        self.enter_date(wd, Date(day_str="29", month_str="June", year_str="1995"), "bday", "bmonth", "byear")
        self.enter_date(wd, Date(day_str="1", month_str="January", year_str="2000"), "aday", "amonth", "ayear")

        Select(wd.find_element_by_name("new_group")).select_by_index(0)
        wd.find_element_by_name("address2").send_keys("address test")
        wd.find_element_by_name("phone2").send_keys("00000000")
        wd.find_element_by_name("notes").send_keys("notes test")

        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def open_add_contact_page(self, wd):
        wd.find_element_by_link_text("add new").click()

    def enter_date(self, wd, date, elname_day, elname_month, elname_year):
        Select(wd.find_element_by_name(elname_day)).select_by_visible_text(date.day)
        Select(wd.find_element_by_name(elname_month)).select_by_visible_text(date.month)
        wd.find_element_by_name(elname_year).send_keys(date.year)

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.wd.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
