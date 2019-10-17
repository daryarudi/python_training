import re


def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert clear(contact_from_home_page.hphone) == clear(contact_from_edit_page.hphone)
    assert clear(contact_from_home_page.mphone) == clear(contact_from_edit_page.mphone)
    assert clear(contact_from_home_page.wphone) == clear(contact_from_edit_page.wphone)


def test_phones_on_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert clear(contact_from_view_page.hphone) == clear(contact_from_edit_page.hphone)
    assert clear(contact_from_view_page.mphone) == clear(contact_from_edit_page.mphone)
    assert clear(contact_from_view_page.wphone) == clear(contact_from_edit_page.wphone)


def clear(s):
    return re.sub("[() -]", "", s)
