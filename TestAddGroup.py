# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from group import Group
from log import Log


class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_group(self):
        wd = self.wd
        log = Log(wd, "http://localhost/addressbook/group.php")
        log.open_home_page()
        log.login(username="admin", password="secret")
        self.open_groups_page(wd)
        self.create_group(wd, Group(name="test", header="test test", footer="test teest"))
        self.open_groups_page(wd)
        log.logout()

    def test_add_empty_group(self):
        wd = self.wd
        log = Log(wd, "http://localhost/addressbook/group.php")
        log.open_home_page()
        log.login(username="admin", password="secret")
        self.open_groups_page(wd)
        self.create_group(wd, Group(name="", header="", footer=""))
        self.open_groups_page(wd)
        log.logout()

    def create_group(self, wd, group):
        wd.find_element_by_name("new").click()

        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").send_keys(group.footer)

        wd.find_element_by_name("submit").click()

    def open_groups_page(self, wd):
        wd.find_element_by_link_text("groups").click()

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
