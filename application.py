from selenium import webdriver
from selenium.webdriver.support.ui import Select


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

# log
    def login(self, username, password):
        wd = self.wd
        wd.get("http://localhost/addressbook/group.php")
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def destroy(self):
        wd = self.wd
        wd.quit()

# groups
    def create_group(self, group):
        wd = self.wd
        self.open_groups_page()
        wd.find_element_by_name("new").click()

        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").send_keys(group.footer)

        wd.find_element_by_name("submit").click()

    def open_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()

# contacts
    def create_contact(self, contact):
        wd = self.wd
        self.open_add_contact_page()
        contact.add_emails("email1@mail.test", "email2@mail.test", "email3@mail.test")
        # contact.add_phone_numbers("00000000", "00000000", "00000000", "00000000")
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
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").send_keys(contact.home)
        wd.find_element_by_name("mobile").send_keys(contact.mobile)
        wd.find_element_by_name("work").send_keys(contact.work)
        wd.find_element_by_name("fax").send_keys(contact.fax)
        wd.find_element_by_name("email").send_keys(contact.email1)
        wd.find_element_by_name("email2").send_keys(contact.email2)
        wd.find_element_by_name("email3").send_keys(contact.email3)
        Select(wd.find_element_by_name("new_group")).select_by_index(contact.group)

    def open_add_contact_page(self):
        wd = self.wd
        wd.find_element_by_link_text("add new").click()
