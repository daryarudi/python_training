# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact("fname1", "mname1", "lname", "nname", "title", "company", "address"))
