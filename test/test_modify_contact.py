from pythoncourse2020.model.contact import Contact
from random import randrange

def test_modify_some_contact(app):
    if app.contact.count_contact() == 0:
        app.contact.create(Contact(first_name="test_name1", midle_name="test_midle_name1", last_name="test_last_name1", nikname="test_nikname1"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact_new = Contact(first_name="test_name4001", midle_name="midle_name4002", last_name="last_name4003")
    contact_new.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact_new)
    assert len(old_contacts) == app.contact.count_contact()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact_new
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
