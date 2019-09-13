from selenium.webdriver.support.ui import Select


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.open_add_contact_page()
        self.enter_contact_info(contact)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.open_add_contact_page()

    def modify_first_contact(self, contact):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_element_by_xpath("(//img[@alt='Edit'])").click()
        self.enter_contact_info(contact)
        wd.find_element_by_name("update").click()
        self.open_contact_page()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def enter_contact_info(self, contact):
        self.change_field_value("firstname", contact.fname)
        self.change_field_value("middlename", contact.mname)
        self.change_field_value("lastname", contact.lname)
        self.change_field_value("nickname", contact.nname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("(//input[@value='Delete'])").click()
        wd.switch_to_alert().accept()
        self.open_contact_page()

    def open_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def open_add_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
