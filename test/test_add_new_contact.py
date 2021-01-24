# -*- coding: utf-8 -*-
from pythoncourse2020.model.contact import Contact
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [
    Contact(first_name=random_string("first_name", 10), midle_name=random_string("midle_name", 20), last_name=random_string("last_name", 20))
    for name in range(1)
]
@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    pass
    old_contacts = app.contact.get_contact_list()
    #contact = Contact(first_name="test_name", midle_name="midle_name", last_name="last_name", address ="Ni No 2", homephone="1111111111",
                      #workphone="22222222", mobilephone="33333333", email="test11@mail.ru", email2="test22@mail.ru", email3="test33@mail.ru",
                      #secondaryphone="4444444")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count_contact()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
