from model.contact import Contact
import re


def test_comparator_contact_on_home_page_and_db(app, db):
    if len(db.get_group_list()) == 0:
        app.contact.create(Contact(firstname="test_name1",  lastname="test_last_name1"))
    contacts_home_page = app.contact.get_contact_list()
    contacts_db = db.get_contact_list()
    list_contacts_from_home_page = list(
        map(lambda y: (y.id, y.firstname, y.lastname, y.all_emails_from_home_page, y.all_phones_from_home_page), contacts_home_page ))
    list_contacts_from_db = list(
        map(lambda y: (y.id, y.firstname, y.lastname, merge_emails_like_on_home_page(y), merge_phones_like_on_home_page(y)), contacts_db))
    assert sorted(list_contacts_from_home_page) == sorted(list_contacts_from_db)



def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobile, contact.work]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda y: y != "", filter(lambda y: y is not None, [contact.email, contact.email2, contact.email3])))