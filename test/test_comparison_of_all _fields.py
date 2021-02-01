from pythoncourse2020.model.contact import Contact
import re
from random import randrange

def test_comparison_of_all_fields_on_home_page_and_edit_page(app):
    if app.contact.count_contact() == 0:
        app.contact.create(Contact(first_name="test_name", midle_name="midle_name", last_name="last_name", address ="NiNo2", homephone="1111111111",
                      workphone="22222222", mobilephone="33333333", email="test2@mail.ru",  secondaryphone="4444444"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.last_name == contact_from_edit_page.last_name
    assert contact_from_home_page.first_name == contact_from_edit_page.first_name
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)

#def test_phones_on_contact_view_page(app):
    #contact_from_view_page = app.contact.get_contact_from_view_page(0)
    #contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    #assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    #assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
    #assert contact_from_view_page.workphone == contact_from_edit_page.workphone
    #assert contact_from_view_page.secondaryphone == contact_from_edit_page.secondaryphone

def clear_for_phones(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x:clear_for_phones(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda y: y != "", filter(lambda y: y is not None, [contact.email, contact.email2, contact.email3])))