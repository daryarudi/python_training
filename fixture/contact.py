from selenium.webdriver.support.ui import Select
from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def count(self):
        wd = self.app.wd
        self.open_contact_page()
        return len(wd.find_elements_by_name("selected[]"))

    def create(self, contact):
        wd = self.app.wd
        self.open_add_contact_page()
        self.enter_contact_info(contact)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.open_add_contact_page()
        self.contact_cache = None

    def modify_first_contact(self, contact):
        self.modify_contact_by_index(0, contact)

    def modify_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_elements_by_xpath("(//img[@alt='Edit'])")[index].click()
        self.enter_contact_info(contact)
        wd.find_element_by_name("update").click()
        self.open_contact_page()
        self.contact_cache = None

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def enter_contact_info(self, contact):
        self.change_field_value("firstname", contact.fname)
        self.change_field_value("middlename", contact.mname)
        self.change_field_value("lastname", contact.lname)
        self.change_field_value("home", contact.hphone)
        self.change_field_value("mobile", contact.mphone)
        self.change_field_value("work", contact.wphone)
        self.change_field_value("fax", contact.fax)

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_xpath("(//input[@value='Delete'])").click()
        wd.switch_to_alert().accept()
        self.open_contact_page()
        wd.find_element_by_css_selector("div.msgbox")
        self.contact_cache = None

    def open_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/") and len(wd.find_elements_by_xpath("(//input[@value='Delete'])")) > 0):
            wd.find_element_by_link_text("home").click()

    def open_add_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_xpath("(//input[@name='submit'])[2]")) > 0):
            wd.find_element_by_link_text("add new").click()

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contact_page()
            groups = []
            for el in wd.find_elements_by_name("entry"):
                tds = el.find_elements_by_tag_name("td")
                lname = tds[1].text
                fname = tds[2].text
                id = tds[0].find_element_by_tag_name("input").get_attribute("value")
                groups.append(Contact(fname=fname, lname=lname, id=id))
        return groups
