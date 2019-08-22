class Contact:

    def __init__(self, group_id, fname, mname, lname, nname, title, company, address):
        self.fname = fname
        self.mname = mname
        self.lname = lname
        self.nname = nname
        self.title = title
        self.company = company
        self.address = address
        self.group = group_id
        self.init_empty()

    def init_empty(self):
        empty = ""
        self.home = empty
        self.mobile = empty
        self.work = empty
        self.fax = empty
        self.email1 = empty
        self.email2 = empty
        self.email3 = empty

    def add_phone_numbers(self, home, mobile, work, fax):
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax

    def add_emails(self, email1, email2, email3):
        self.email1 = email1
        self.email2 = email2
        self.email3 = email3

