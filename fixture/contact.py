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
        wd = self.app.wd
        self.open_contact_page()
        wd.find_element_by_xpath("(//img[@alt='Edit'])").click()
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
