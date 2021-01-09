# -*- coding: utf-8 -*-
from pythoncourse2020.model.contact import Contact


def test_add_contact(app):
    old_contact = app.contact.get_contact_list()
    app.contact.create(Contact(first_name="test_name", midle_name="test_midle_name", last_name="test_last_name", nikname="test_nikname"))
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) + 1 == len(new_contact)
