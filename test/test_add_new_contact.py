# -*- coding: utf-8 -*-
from pythoncourse2020.model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name="test_name", midle_name="midle_name", last_name="last_name", homephone="1111111111",
                      workphone="22222222", mobilephone="33333333", secondaryphone="4444444")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count_contact()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
