# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest


class Log:
    def __init__(self, wd, homepage):
        self.wd = wd
        self.homepage = homepage

    def open_home_page(self):
        self.wd.get(self.homepage)

    def login(self, username, password):
        self.wd.find_element_by_name("user").send_keys(username)
        self.wd.find_element_by_name("pass").send_keys(password)
        self.wd.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self):
        self.wd.find_element_by_link_text("Logout").click()
