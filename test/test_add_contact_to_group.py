from model.group import Group
from model.contact import Contact
import random


def test_add_contact_in_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test_group_name"))
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test_name1", lastname="test_last_name1"))
    if len(db.get_contacts_not_in_group()) == 0:
        app.contact.create(Contact(firstname="test_name2", lastname="test_last_name2"))
    old_contacts = db.get_contacts_not_in_group()
    contact = random.choice(old_contacts)
    groups = db.get_group_list()
    group = random.choice(groups)
    app.contact.add_contact_in_group(contact.id, group.id)
    new_contacts = db.get_contacts_not_in_group()
    assert len(old_contacts) - 1 == len(new_contacts)

