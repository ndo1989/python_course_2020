from model.contact import Contact
import random

def test_modify_some_contact(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.contact.create(Contact(first_name="test_name1", midle_name="test_midle_name1", last_name="test_last_name1", nikname="test_nikname1"))
    old_contacts = db.get_contact_list()
    edit_contact = random.choice(old_contacts)
    contact_new = Contact(firstname="test_name6001")
    #contact_new.id = old_contacts[index].id
    app.contact.modify_contact_by_id(edit_contact.id, contact_new)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    edit_contact.firstname = contact_new.firstname
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

