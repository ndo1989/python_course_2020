# -*- coding: utf-8 -*-
from pythoncourse2020.model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count_contact() == 0:
        app.contact.create(Contact(first_name="test_name1", midle_name="test_midle_name1", last_name="test_last_name1", nikname="test_nikname1"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    #old_contacts[0:1] = []
    #assert old_contacts == new_contacts