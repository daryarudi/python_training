from selenium.webdriver.support.ui import Select


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.wd
        self.open_add_contact_page()
        self.enter_contact_info(contact)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def enter_contact_info(self, contact):
        wd = self.wd
        wd.find_element_by_name("firstname").send_keys(contact.fname)
        wd.find_element_by_name("middlename").send_keys(contact.mname)
        wd.find_element_by_name("lastname").send_keys(contact.lname)
        wd.find_element_by_name("nickname").send_keys(contact.nname)
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").send_keys(contact.company)
        Select(wd.find_element_by_name("new_group")).select_by_index(contact.group)

    def open_add_contact_page(self):
        wd = self.wd
        wd.find_element_by_link_text("add new").click()
