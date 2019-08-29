# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact("fname_new", "mname_new", "lname_new", "nname", "title", "company", "address"))
    app.session.logout()
