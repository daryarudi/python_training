# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(fname="fname", lname="lname"))
    app.contact.modify_first_contact(Contact(fname="fname_new", lname="lname_new"))
