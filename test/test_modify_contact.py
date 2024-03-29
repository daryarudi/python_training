# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange


def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(fname="fname", lname="lname"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(fname="fname_new", lname="lname_new")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    new_contacts[index] = contact
    assert sorted(new_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
